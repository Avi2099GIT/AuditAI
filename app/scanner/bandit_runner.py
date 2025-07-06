# app/scanner/bandit_runner.py
import logging
import json
import tempfile
import subprocess

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def run_bandit_scan(target_path):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
            command = [
                "bandit", "-r", target_path,
                "-f", "json", "-o", temp_file.name
            ]
            subprocess.run(command, check=True)
            temp_file_path = temp_file.name

        with open(temp_file_path, "r") as f:
            report = json.load(f)

        raw_results = report.get("results", [])
        normalized_results = []

        for item in raw_results:
            normalized_results.append({
                "file": item.get("filename", "N/A"),
                "line": item.get("line_number", -1),
                "type": "Bandit",
                "severity": item.get("issue_severity", "MEDIUM").upper(),
                "confidence": item.get("issue_confidence", "MEDIUM").upper(),
                "description": item.get("issue_text", "No description provided")
            })

        return normalized_results

    except Exception as e:
        logging.error(f"❌ Bandit scan failed: {e}")
        return []
