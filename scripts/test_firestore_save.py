from app.database.firestore_client import save_scan_results
from app.utils.git_utils import get_latest_commit_hash

mock_results = [
    {
        "file_path": "app/example.py",
        "issue_type": "Hardcoded secret",
        "description": "Hardcoded API key found.",
        "severity": "High",
        "line_number": 42,
        "source": "bandit"
    }
]

commit_hash = get_latest_commit_hash()

save_scan_results(
    mock_results,
    project_name="AuditAI Secure",
    commit_hash=commit_hash
)

print("✅ Mock scan results successfully saved to Firestore.")