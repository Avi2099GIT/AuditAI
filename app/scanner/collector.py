import os
from typing import List

def collect_python_files(directory: str) -> List[str]:
    """Recursively collects all .py files in the given directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith("__init__"):
                python_files.append(os.path.join(root, file))
    return python_files
