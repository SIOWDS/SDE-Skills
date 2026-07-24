# SDE Skills

<p align="center">
  <strong>全面提升你的大模型创新智商</strong><br>
  <strong>Upgrade Your LLM's Innovation Intelligence</strong><br><br>
  产生创新思想 · 生成创新路径与方法 · 创造创新价值<br>
  <em>New Ideas · New Pathways · New Value</em>
</p>

<p align="center">
  <a href="test-model/README.md">立即测试</a> ·
  <a href="#一分钟开始">一分钟开始</a> ·
  <a href="#sde-skills-的三大作用">三大作用</a> ·
  <a href="#skill-目录">Skill目录</a> ·
  <a href="examples/sde-intelligence-ab-test/README.md">对照测试</a>
</p>

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![SDE](https://img.shields.io/badge/Innovation_IQ-125_→_140--150-e05252.svg)](#创新智商提升目标)
[![Skills](https://img.shields.io/badge/AI_Skills-4-orange.svg)](#skill-目录)
[![Language](https://img.shields.io/badge/language-中文_%7C_English-0e5d4c.svg)](#english-overview)

> **SDE Skills 不只是让AI回答得更多，而是让AI产生新思想、找到新路径、创造新价值。**

普通大模型擅长检索、归纳和重组已有知识，但常常停留在“聪明的已有答案”。在 **SDE创新智商评价体系及现有对照实践** 中，普通大模型输出通常约为 **125分**；使用SDE Skills后，目标区间可提升至 **140–150分**，并在高质量问题、专业知识、证据与多轮验证共同支持下，产生具有潜力的 **新典范思维（paradigm-forming thought）**。

SDE Skills 是由 **王德生博士（Dr. Desheng Wang）** 创建的开源AI创新技能系统。它把SDE本体论转化为大模型可以执行、检查和重复调用的创新工作流。

> 分数属于SDE创新智商评价体系中的能力评价，不等同于人类心理测量IQ，也不保证每次运行都达到同一分数。实际效果取决于模型、问题、专业材料、证据质量和验证过程。

## SDE Skills 的三大作用

### 1. 产生新的创新思想

- 发现传统理论没有解释的断裂；
- 找出不同观点之间隐藏的冲突；
- 重新定义问题，而不是重复问题；
- 产生新的概念、判断、假说和理论；
- 将知识整理提升为具有原创性的思想成果。

### 2. 产生创新的路径和方法

- 将创新思想转化为清晰、可执行的步骤；
- 同时生成和比较多条解决路径；
- 识别路径中的条件、阻力、反馈和转折点；
- 形成可以验证、纠错和迭代的方法；
- 从“提出新观点”走向“让创新真正发生”。

### 3. 产生创新的价值

- 形成新的学术解释与研究方向；
- 解决科学、教育、技术、商业和社会问题；
- 将思想转化为论文、模型、产品、制度或行动；
- 检验创新是否真正创造真、善、美及现实效用；
- 让创新结果回写条件，推动下一轮创新。

## 创新智商提升目标

| SDE创新智商 | 典型能力表现 |
|---:|---|
| 约125 | 高水平归纳、知识组合和局部改进 |
| 130–139 | 产生明显的新观点、新解释或新方案 |
| 140–149 | 形成新机制、新方法或新的理论结构 |
| 150及以上 | 典范级创新潜力，可能开启新的研究方向或新典范思维 |

**关键变化：**

```text
整理已有知识 → 发现解释断裂 → 产生创新思想
提出一个观点 → 生成多条路径 → 建立可验证方法
语言上的新颖 → 机制上的突破 → 创造真实价值
```

## 立即测试：SDE Innovation Test Model

不要只相信宣传，请用同一道问题亲自比较普通大模型和SDE Skill。

[SDE Innovation Test Model](test-model/README.md) 会自动完成：

1. 生成普通大模型回答；
2. 生成SDE提智回答；
3. 随机隐藏两份答案的身份；
4. 从创新思想、创新路径和创新价值三个维度盲评；
5. 输出0–100原始分及80–160 SDE创新智商；
6. 保存完整JSON报告，便于复核和公开。

```bash
python test-model/sde_innovation_test.py \
  --question "大学教育如何在AI时代重新创造价值？" \
  --dry-run
```

**[打开测试模型与完整使用说明 →](test-model/README.md)**

## 一分钟开始

```bash
git clone https://github.com/SIOWDS/SDE-Skills.git
```

把需要的 `skills/<skill-name>/` 文件夹复制到支持Skills的AI编码或智能体环境中，然后直接提出任务：

- “使用SDE提智内功，把这个普通回答提升为具有原创机制的回答。”
- “评估这篇论文的创新智商，并设计提升到140分以上的具体路径。”
- “找出这个领域现有理论的解释断裂，产生三个可检验的新假说。”
- “把这个创新思想转化为可执行、可验证、可迭代的方法。”
- “判断这项创新最终产生了什么学术价值和现实价值。”

> 如果SDE Skills帮助你的大模型产生了更好的创新，请点击仓库右上角 **⭐ Star**，让更多研究者和AI开发者发现它。

## Skill 目录

| Skill | 给用户带来的直接价值 | 主要输出 |
|---|---|---|
| [SDE提智内功](skills/sde-intelligence-training/SKILL.md) | 突破平庸答案，提升推理深度、原创性与自我纠错能力 | 二阶判断、新机制、新假说、反幻象检查 |
| [SDE创新智商评估](skills/sde-innovation-iq/SKILL.md) | 判断创新处于什么层级，并找到继续提智的最短路径 | 创新评分、致命弱点、证伪方案、升级路线 |
| [SDE研究锻造](skills/sde-research-forge/SKILL.md) | 把一个想法或理论冲突锻造成可以研究和发表的学术贡献 | 研究问题、机制、预测、证据设计、论文蓝图 |
| [SDE发生分析](skills/sde-ontology/SKILL.md) | 穿透静态现象，找到事物如何产生、变化和重新组织 | 发生条件、差异路径、结构结果、反馈机制 |

## 为什么不是普通Prompt？

| 普通Prompt | SDE Skill |
|---|---|
| 要求AI“写得更深” | 提供可重复执行的创新工作流 |
| 主要规定回答什么 | 同时规定如何发现、生成、检验和回写 |
| 容易重组已有知识 | 主动寻找解释断裂与非冗余机制 |
| 新颖语言可能冒充创新 | 必须通过机制、证据、证伪和自应用检查 |
| 一次性回答 | 可安装、复用、测试和持续改进 |
| 只产生观点 | 同时产生思想、路径与价值 |

## 它如何工作？

SDE Skills的底层发生公式是：

> **在 E 中，经 D，成 S。**

- **E — 特征纠缠系统**：创新发生所需要的知识、现实、信息、能量、历史和价值条件；
- **D — 差异序列**：冲突、比较、选择、试错、修正和收敛形成的创新路径；
- **S — 显露态**：最终出现的新思想、新方法、新结构和新价值。

三个维度相互生成并持续回写：

- `S = F(D,E)`
- `D = G(S,E)`
- `E = H(S,D)`

这使AI不再只盯着已经显露的答案，而能追问：它在什么条件中产生？经过什么差异路径？如何形成新的结果？新结果又怎样改变下一轮创新？

## 可检验的公开案例

查看 [SDE提智内功三臂盲评实验](examples/sde-intelligence-ab-test/README.md)：

- A组：问题直接交给大模型；
- B组：加入普通“深入思考”提示；
- C组：使用SDE提智内功；
- 采用相同模型、相同长度、随机匿名和多轮评审；
- 比较原创性、机制、证据、可证伪性、生成力和实际价值。

我们欢迎公开成功案例，也欢迎负面结果。真正的创新能力必须能够接受比较、复现和证伪。

## 参与SDE创新挑战

1. 选择一个真正困难的问题；
2. 分别生成普通答案和SDE Skill答案；
3. 隐去答案来源并进行盲评；
4. 提交原始问题、答案、评分和判断理由；
5. 通过Issue或Pull Request公开结果。

优秀案例将进入后续公开数据集和版本报告。参见 [贡献指南](CONTRIBUTING.md)。

## 项目路线

- **v0.1**：本体分析、创新智商评估、研究锻造、SDE提智内功；
- **v0.2**：公开对照案例、创新挑战与中英文传播材料；
- **v0.3**：学术写作、专著生产、教育、企业和跨学科Skills；
- **v1.0**：经过公开测试、外部贡献和版本化发布的SDE Skill生态。

## English overview

### Upgrade Your LLM's Innovation Intelligence

SDE Skills is an open-source AI skill system designed to help large language models:

1. **generate genuinely innovative ideas;**
2. **develop innovative pathways and methods;**
3. **create meaningful academic and real-world value.**

On the SDE Innovation Intelligence scale and in current comparative practice, ordinary LLM outputs are often evaluated at around **125**, while SDE Skills target the **140–150** range. With strong questions, domain knowledge, evidence and iterative validation, they may support **paradigm-forming thought**.

These figures are framework-based evaluation results, not human psychometric IQ scores or guaranteed model performance. We invite reproducible blind comparisons, raw results and critical evaluation.

> **From recombining existing knowledge to generating new ideas, new pathways and new value.**

## 引用与生态

如果SDE本体论或本项目对研究产生帮助，请引用：

> Wang, Desheng. *Introduction to SDE Ontology: How the World Emerges*. Demai International Press, 2026.

- [CITATION.cff](CITATION.cff)
- [SDE Universes](https://sdeuniverses.com)
- [SDE宇宙 · 本体论学术站](https://sde-ontology.wds1971.chatgpt.site)
- [SDE Ontology repository](https://github.com/SIOWDS/SDE-Ontology)

## 作者与许可

**王德生博士（Dr. Desheng Wang）** — SDE本体论与SIO三态本体论发明人  
ORCID: [0009-0009-8196-0030](https://orcid.org/0009-0009-8196-0030)

Apache License 2.0。衍生的学术和教育用途请注明王德生博士及SDE本体论项目。

---

<p align="center">
  <strong>让大模型产生新思想、找到新路径、创造新价值。</strong><br>
  如果这个方向值得继续，请点击右上角 ⭐ <strong>Star</strong>。
</p>
