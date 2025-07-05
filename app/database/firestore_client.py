import os
import json
from dotenv import load_dotenv
from google.cloud import firestore

load_dotenv()

def get_firestore_client():
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        raise ValueError("Firestore credentials not found.")
    return firestore.Client.from_service_account_json(cred_path)

def save_scan_results(scan_results):
    client = get_firestore_client()
    collection = client.collection("audit_results")

    for result in scan_results:
        doc_ref = collection.document()
        doc_ref.set(result)
