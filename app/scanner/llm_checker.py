# app/scanner/llm_checker.py
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

import os
from app.utils.code_utils import extract_code_blocks
from app.utils.llm_utils import analyze_code_with_llm

def run_llm_checks(file_paths):
    results = []

    for file_path in file_paths:
        try:
            code_blocks = extract_code_blocks(file_path)

            for block in code_blocks:
                prompt = (
                    "You are a security code auditor. Analyze the following Python code "
                    "for any vulnerabilities or bad practices. Respond with issue type, description, severity level, and line number.\n\n"
                    f"{block['code']}"
                )

                issues = analyze_code_with_llm(prompt)

                for issue in issues:
                    results.append({
                        "file_path": file_path,
                        "issue_type": issue.get("issue_type", "Unknown"),
                        "description": issue.get("description", "No description provided"),
                        "severity": issue.get("severity", "Medium"),
                        "line_number": block["line_number"],
                        "source": "llm"
                    })

        except Exception as e:
            print(f"❌ LLM check failed for {file_path}: {e}")

    return results
