from app.scanner.collector import collect_python_files
from app.scanner.bandit_runner import run_bandit_on_files
from app.database.firestore_client import save_scan_results

if __name__ == "__main__":
    files = collect_python_files("app")
    print(f"Scanning {len(files)} files...")
    results = run_bandit_on_files(files)

    save_scan_results(results)
    print(f"Saved {len(results)} results to Firestore.")
