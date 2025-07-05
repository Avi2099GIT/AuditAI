import os
import json
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import firestore

load_dotenv()

def get_firestore_client():
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        raise ValueError("Firestore credentials not found.")
    return firestore.Client()

def save_scan_results(scan_results, project_name=None, commit_hash=None):
    client = get_firestore_client()
    collection = client.collection("audit_results")

    metadata = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "project_name": project_name or "unknown_project",
        "commit_hash": commit_hash or "unknown_commit",
    }

    for result in scan_results:
        result_with_meta = {**result, **metadata}
        doc_ref = collection.document()
        doc_ref.set(result_with_meta)
