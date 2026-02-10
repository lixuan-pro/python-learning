import os
import json
from openai import OpenAI


def analyze_scores_with_ai(stats):
    prompt = build_prompt(stats)
    return call_llm(prompt)


def build_prompt(stats):
    """
    stats 是一个 dict，例如：
    {
      "scores": [
        {"name": "Alice", "score": 95},
        {"name": "Charlie", "score": 88}
      ],
      "max": 95,
      "min": 76,
      "average": 86.3
    }
    """

    stats_json = json.dumps(stats, ensure_ascii=False, indent=2)

    return f"""
你是一个数据分析师和结果检查员。

下面提供的是【已经由程序计算完成的成绩统计结果】，
这些数据是最终事实，请你【不要修改其中任何数值】。

你的任务是：
1. 检查数据结构是否合理
2. 基于这些结果，用自然语言给出简要分析
3. 不要重新计算分数

成绩统计结果如下（JSON）：
{stats_json}

请直接给出分析文本，不要重复 JSON。
"""


def call_llm(prompt):
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
