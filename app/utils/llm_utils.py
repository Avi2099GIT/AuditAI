# app/utils/llm_utils.py

import os
import json
from together import Together

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def analyze_code_with_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": "You are a Python security auditor. Reply in JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content
        issues = json.loads(content)
        return issues if isinstance(issues, list) else []

    except Exception as e:
        print(f"❌ LLM call failed: {e}")
        return []
