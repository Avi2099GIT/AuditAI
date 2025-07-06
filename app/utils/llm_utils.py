# app/utils/llm_utils.py

import os
import json
import requests

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_code_with_llm(prompt):
    try:
        data = {
            "model": "meta-llama-3-8b-instruct",  # Use any supported Together model
            "messages": [
                {"role": "system", "content": "You are a Python security auditor."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }

        response = requests.post(TOGETHER_API_URL, headers=headers, json=data)
        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]

        # Parse JSON content (expected to be a list of issues)
        issues = json.loads(content)
        return issues if isinstance(issues, list) else []

    except Exception as e:
        print(f"❌ LLM call failed: {e}")
        return []