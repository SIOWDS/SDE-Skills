# SDE Innovation Test Model

这是一个可以直接运行的盲测模型，用同一道问题比较：

- **Baseline**：大模型直接回答；
- **SDE**：大模型使用SDE提智内功后回答；
- **Blind Judge**：随机隐藏答案来源，再按统一标准评分。

测试聚焦SDE Skills的三大作用：

1. **创新思想（40分）**
2. **创新路径和方法（35分）**
3. **创新价值（25分）**

原始量表为0–100分。为了与SDE创新智商表达体系对接，程序透明换算：

```text
SDE创新智商 = 80 + 0.8 × 原始得分
```

因此：

| 原始得分 | SDE创新智商 |
|---:|---:|
| 56.25 | 125 |
| 75 | 140 |
| 87.5 | 150 |
| 100 | 160 |

该分数是SDE框架内的比较性评价，不是人类心理测量IQ，也不保证每次运行达到固定分数。

## 运行要求

- Python 3.10或更高版本；
- 一个兼容OpenAI Chat Completions格式的API；
- 不需要安装第三方Python包。

## 第一步：设置环境变量

Linux/macOS：

```bash
export SDE_API_KEY="你的API密钥"
export SDE_MODEL="你的回答模型"
export SDE_JUDGE_MODEL="你的评审模型"
export SDE_API_BASE="https://api.openai.com/v1"
```

Windows PowerShell：

```powershell
$env:SDE_API_KEY="你的API密钥"
$env:SDE_MODEL="你的回答模型"
$env:SDE_JUDGE_MODEL="你的评审模型"
$env:SDE_API_BASE="https://api.openai.com/v1"
```

不要把API密钥写进代码、测试报告或提交到GitHub。

## 第二步：先做无API检查

```bash
python test-model/sde_innovation_test.py \
  --question "大学教育如何在AI时代重新创造价值？" \
  --dry-run
```

## 第三步：运行正式盲测

```bash
python test-model/sde_innovation_test.py \
  --question "大学教育如何在AI时代重新创造价值？" \
  --output sde-test-report.json
```

程序将输出两组创新智商，并把问题、匿名标签、完整答案、维度得分和评审理由保存为JSON报告。

## 如何提高可信度

单次运行只能展示方法，不能证明普遍提升。正式实验应当：

- 使用至少30个跨领域问题；
- 每个条件重复至少3次；
- 使用两个以上评审模型；
- 增加人类专业评审；
- 控制答案长度与提示长度；
- 完整公开成功、失败和负面案例。

更严格的研究设计参见：

[SDE提智内功三臂盲评实验](../examples/sde-intelligence-ab-test/README.md)
