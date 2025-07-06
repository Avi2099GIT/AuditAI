import os
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import firestore

load_dotenv()

def get_firestore_client():
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        raise ValueError("Firestore credentials not found at: {}".format(cred_path))
    return firestore.Client()

def save_scan_results(scan_results, project_name=None, commit_hash=None):
    client = get_firestore_client()
    collection = client.collection("audit_results")

    # Schema fields that must exist in every record
    required_fields = {
        "file": "unknown_file",
        "line": -1,
        "type": "UNKNOWN",
        "severity": "LOW",  # Can be LOW/MEDIUM/HIGH
        "confidence": "LOW",  # Can be LOW/MEDIUM/HIGH
        "description": "No description provided"
    }

    # Metadata common to all results in this run
    metadata = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "project_name": project_name or "unknown_project",
        "commit_hash": commit_hash or "unknown_commit",
    }

    for result in scan_results:
        # Apply schema defaults
        validated_result = {key: result.get(key, default) for key, default in required_fields.items()}

        # Merge validated result with metadata
        result_with_meta = {**validated_result, **metadata}

        # Save to Firestore
        doc_ref = collection.document()
        doc_ref.set(result_with_meta)
