# app/scanner/analyzer.py
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

from app.scanner.collector import collect_python_files
from app.scanner.bandit_runner import run_bandit_scan
from app.scanner.llm_checker import run_llm_checks
from app.database.firestore_client import save_scan_results

def run_full_analysis(path="."):
    logging.info(f"🔍 Collecting Python files from {path}...")
    files = collect_python_files(path)

    all_results = []

    # Static analysis with Bandit
    logging.info("🛡 Running Bandit static analysis...")
    bandit_results = run_bandit_scan(files)
    all_results.extend(bandit_results)

    # AI-based checks
    logging.info("🤖 Running LLM-based code checks...")
    llm_results = run_llm_checks(files)
    all_results.extend(llm_results)

    logging.info(f"✅ Total issues found: {len(all_results)}")

    if all_results:
        logging.info("💾 Saving scan results to Firestore...")
        save_scan_results(all_results)
        logging.info("✅ Results saved to Firestore.")

    return all_results
