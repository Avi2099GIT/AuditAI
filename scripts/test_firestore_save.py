from app.database.firestore_client import save_scan_results

# Mock scan result
mock_results = [
    {
        "file": "app/main.py",
        "issue": "Hardcoded secret found",
        "severity": "HIGH",
        "line": 42,
        "description": "This line contains a hardcoded secret which should be moved to environment variables."
    },
    {
        "file": "app/utils/crypto.py",
        "issue": "Insecure hash function",
        "severity": "MEDIUM",
        "line": 12,
        "description": "MD5 is not recommended for cryptographic purposes. Use SHA-256 or stronger."
    }
]

# Save to Firestore
save_scan_results(mock_results)
print("✅ Mock scan results successfully saved to Firestore.")
