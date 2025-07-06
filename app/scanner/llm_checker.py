# app/scanner/llm_checker.py
import logging
from app.utils.code_utils import extract_code_blocks
from app.utils.llm_utils import analyze_code_with_llm

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

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
                        "file": file_path,
                        "line": issue.get("line_number", block.get("line_number", -1)),
                        "type": "LLM",
                        "severity": issue.get("severity", "MEDIUM").upper(),
                        "confidence": issue.get("confidence", "MEDIUM").upper(),
                        "description": issue.get("description", "No description provided")
                    })

        except Exception as e:
            logging.error(f"❌ LLM check failed for {file_path}: {e}")

    return results