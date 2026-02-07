import os
from openai import OpenAI

def analyze_scores_with_ai(student_scores):
    prompt = build_prompt(student_scores)
    return call_llm(prompt)


def build_prompt(student_scores):
    scores_text = "\n".join(
        [f"{name}: {score}" for name, score in student_scores.items()]
    )

    return f"""
你是一个数据分析助手。
下面是学生成绩数据：

{scores_text}

请用自然语言给出简要分析，包括：
1. 整体水平
2. 是否存在明显高分或低分
3. 简单建议
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
