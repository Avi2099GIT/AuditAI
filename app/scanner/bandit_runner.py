# app/scanner/bandit_runner.py
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

import json
import tempfile
import subprocess

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

        return report.get("results", [])
    except Exception as e:
        logging.error(f"❌ Bandit scan failed: {e}")
        return []
