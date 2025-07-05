import subprocess
import json

def run_bandit_on_files(file_paths):
    results = []
    for file in file_paths:
        try:
            output = subprocess.check_output(
                ["bandit", "-f", "json", "-q", file],
                stderr=subprocess.DEVNULL,
                text=True
            )
            data = json.loads(output)
            results.append({
                "file": file,
                "issues": data.get("results", [])
            })
        except subprocess.CalledProcessError:
            continue  # Skip problematic files
    return results
