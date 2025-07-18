# scripts/run_analysis.py
from app.scanner.analyzer import run_full_analysis
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

if __name__ == "__main__":
    results = run_full_analysis(".")
    logging.info("🎉 Analysis complete!")