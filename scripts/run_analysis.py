# scripts/run_analysis.py
from app.scanner.analyzer import run_full_analysis

if __name__ == "__main__":
    results = run_full_analysis(".")
    print("🎉 Analysis complete!")
