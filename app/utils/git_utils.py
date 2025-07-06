# app/utils/git_utils.py

import subprocess

def get_latest_commit_hash():
    try:
        result = subprocess.check_output(["git", "rev-parse", "HEAD"])
        return result.decode().strip()
    except Exception:
        return "unknown_commit"