from google.cloud import firestore
import os
from dotenv import load_dotenv

load_dotenv()

def backfill_confidence():
    db = firestore.Client()
    collection_ref = db.collection("audit_results")

    docs = collection_ref.stream()
    updated = 0

    for doc in docs:
        data = doc.to_dict()
        if "confidence" not in data:
            doc.reference.update({"confidence": "N/A"})
            updated += 1

    print(f"✅ Backfilled confidence field in {updated} documents.")

if __name__ == "__main__":
    backfill_confidence()
