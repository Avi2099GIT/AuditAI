# app/utils/llm_utils.py

import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_code_with_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or your preferred Together AI model
            messages=[
                {"role": "system", "content": "You are a Python security auditor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content

        # Assume LLM replies with JSON-like list of issues
        issues = json.loads(content)
        return issues if isinstance(issues, list) else []

    except Exception as e:
        print(f"❌ LLM call failed: {e}")
        return []
