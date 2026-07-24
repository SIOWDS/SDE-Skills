#!/usr/bin/env python3
"""Provider-neutral A/B test for SDE innovation intelligence."""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SDE_PROMPT = """You are using SDE Innovation Training.
Your goal is not to make the answer merely longer or more polished.
Produce:
1. a genuinely new idea by locating an explanatory fracture;
2. an innovative pathway or method with conditions, steps, feedback and tests;
3. innovative academic or practical value.
Treat the first plausible answer as a hypothesis. Distinguish evidence from
interpretation and speculation. State a falsification condition. Use the
target field's normal language rather than decorative SDE terminology.
"""

JUDGE_PROMPT = """You are a strict blind evaluator of innovation.
Score each answer independently using this 100-point rubric:
- Innovative thought (0-40): explanatory fracture, non-redundant concept,
  originality beyond recombination.
- Innovative pathway (0-35): mechanism, executable steps, feedback,
  falsifiability and validation design.
- Innovative value (0-25): academic/practical consequence, usefulness,
  boundary awareness and credible value creation.

Do not reward verbosity, confidence, jargon or SDE terminology. Penalize
invented facts and unsupported claims. Return JSON only:
{
  "answers": {
    "X": {
      "innovative_thought": 0,
      "innovative_pathway": 0,
      "innovative_value": 0,
      "total": 0,
      "reason": "..."
    },
    "Y": {
      "innovative_thought": 0,
      "innovative_pathway": 0,
      "innovative_value": 0,
      "total": 0,
      "reason": "..."
    }
  },
  "winner": "X or Y or tie",
  "confidence": "low, medium or high"
}
"""


def chat(endpoint: str, api_key: str, model: str, messages: list[dict], temperature: float) -> str:
    url = endpoint.rstrip("/") + "/chat/completions"
    payload = json.dumps(
        {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"API connection failed: {exc}") from exc
    return data["choices"][0]["message"]["content"]


def parse_json(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(cleaned)


def innovation_iq(raw_total: float) -> float:
    """Map the transparent 0-100 rubric to the SDE 80-160 communication scale."""
    return round(80 + 0.8 * max(0, min(100, raw_total)), 1)


def validate_scores(judgment: dict) -> None:
    for label, score in judgment["answers"].items():
        fields = {
            "innovative_thought": 40,
            "innovative_pathway": 35,
            "innovative_value": 25,
            "total": 100,
        }
        for field, maximum in fields.items():
            value = score[field]
            if not isinstance(value, (int, float)) or not 0 <= value <= maximum:
                raise ValueError(f"Invalid {field} for answer {label}: {value}")
        calculated = (
            score["innovative_thought"]
            + score["innovative_pathway"]
            + score["innovative_value"]
        )
        if abs(calculated - score["total"]) > 0.01:
            raise ValueError(f"Score total mismatch for answer {label}")
        score["sde_innovation_iq"] = innovation_iq(score["total"])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Blindly compare a baseline LLM answer with an SDE-trained answer."
    )
    parser.add_argument("--question", help="Question to test")
    parser.add_argument("--question-file", type=Path, help="UTF-8 text file containing the question")
    parser.add_argument("--model", default=os.getenv("SDE_MODEL", "gpt-4.1"))
    parser.add_argument("--judge-model", default=os.getenv("SDE_JUDGE_MODEL"))
    parser.add_argument(
        "--endpoint",
        default=os.getenv("SDE_API_BASE", "https://api.openai.com/v1"),
        help="OpenAI-compatible API base",
    )
    parser.add_argument("--output", type=Path, default=Path("sde-test-report.json"))
    parser.add_argument("--dry-run", action="store_true", help="Validate setup without calling an API")
    args = parser.parse_args()

    question = args.question
    if args.question_file:
        question = args.question_file.read_text(encoding="utf-8").strip()
    if not question:
        parser.error("provide --question or --question-file")

    judge_model = args.judge_model or args.model
    if args.dry_run:
        print(json.dumps(
            {
                "status": "ready",
                "model": args.model,
                "judge_model": judge_model,
                "endpoint": args.endpoint,
                "question": question,
                "rubric_total": 100,
                "iq_mapping": "80 + 0.8 × rubric_total",
            },
            ensure_ascii=False,
            indent=2,
        ))
        return 0

    api_key = os.getenv("SDE_API_KEY")
    if not api_key:
        print("Missing SDE_API_KEY environment variable.", file=sys.stderr)
        return 2

    baseline = chat(
        args.endpoint,
        api_key,
        args.model,
        [{"role": "user", "content": question}],
        0.7,
    )
    trained = chat(
        args.endpoint,
        api_key,
        args.model,
        [
            {"role": "system", "content": SDE_PROMPT},
            {"role": "user", "content": question},
        ],
        0.7,
    )

    pairs = [("baseline", baseline), ("sde", trained)]
    random.SystemRandom().shuffle(pairs)
    labels = {"X": pairs[0], "Y": pairs[1]}
    blind_text = "\n\n".join(
        f"ANSWER {label}\n{answer}" for label, (_, answer) in labels.items()
    )
    judgment_text = chat(
        args.endpoint,
        api_key,
        judge_model,
        [
            {"role": "system", "content": JUDGE_PROMPT},
            {"role": "user", "content": f"QUESTION\n{question}\n\n{blind_text}"},
        ],
        0.0,
    )
    judgment = parse_json(judgment_text)
    validate_scores(judgment)

    decoded = {}
    for label, (arm, answer) in labels.items():
        decoded[arm] = {
            "blind_label": label,
            "answer": answer,
            "score": judgment["answers"][label],
        }

    report = {
        "test_model": "SDE Innovation Test Model v0.1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "question": question,
        "answer_model": args.model,
        "judge_model": judge_model,
        "endpoint": args.endpoint,
        "arms": decoded,
        "blind_judgment": judgment,
        "score_note": (
            "SDE Innovation IQ = 80 + 0.8 × rubric score. "
            "It is a framework-based comparison, not human psychometric IQ."
        ),
    }
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    for arm in ("baseline", "sde"):
        score = decoded[arm]["score"]
        print(
            f"{arm:8} raw={score['total']:5.1f}/100 "
            f"SDE-IQ={score['sde_innovation_iq']:5.1f}"
        )
    print(f"Report written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
