# 🚨 AuditAI



AuditAI is an **AI-powered code auditing and security scanning tool** designed for modern DevSecOps pipelines. It leverages **static analysis** (via Bandit) and **LLM-based code review** (via Together AI or OpenAI) to detect potential vulnerabilities in Python codebases and integrates seamlessly into GitHub PR workflows.

---

## 🔧 Features

- 🧠 **LLM-Powered Security Analysis**\
  Uses Together AI or OpenAI models to identify suspicious code patterns.

- 🔍 **Bandit Static Scanner**\
  Performs traditional static code analysis on Python files.

- 📦 **CI/CD Integration**\
  GitHub Actions-based PR analysis and reporting with automated commenting.

- ☁️ **Firestore Logging**\
  Saves scan results to Google Firestore for long-term tracking or dashboard integration.

- 🧾 **Git Commit Context**\
  Annotates each analysis with current Git commit info (hash, branch, etc).

---

## 📁 Project Structure

```
AuditAI/
│
├── app/
│   ├── scanner/
│   │   ├── analyzer.py
│   │   ├── bandit_runner.py
│   │   ├── collector.py
│   │   └── llm_checker.py
│   ├── utils/
│   │   ├── code_utils.py
│   │   └── llm_utils.py
│   └── database/
│       └── firestore_client.py
│
├── scripts/
│   └── run_analysis.py
│
├── .github/
│   └── workflows/
│       └── pr-audit.yml
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Avi2099GIT/AuditAI.git
cd AuditAI
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root:

```env
TOGETHER_API_KEY=your_together_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/firebase-key.json
```

Also make sure to export the path or use this in GitHub Actions secrets:

- `TOGETHER_API_KEY`
- `GOOGLE_APPLICATION_CREDENTIALS_JSON` (base64/inline contents of the key file)

---

## 🚀 Usage

### Local analysis:

```bash
python scripts/run_analysis.py app/
```

### GitHub Actions:

Add or modify `.github/workflows/pr-audit.yml` to include:

```yaml
name: PR Audit with AI Security Scan

on:
  pull_request:
    branches: [main, dev]

jobs:
  audit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Set up environment variables
        run: |
          echo "TOGETHER_API_KEY=${{ secrets.TOGETHER_API_KEY }}" >> $GITHUB_ENV
          echo '${{ secrets.GOOGLE_APPLICATION_CREDENTIALS_JSON }}' > gcp-key.json
          echo "GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/gcp-key.json" >> $GITHUB_ENV

      - name: Run AuditAI Analysis
        run: |
          PYTHONPATH=. python scripts/run_analysis.py app/ > result.json
```

---

## 📬 Output Format

The result is saved as a JSON file (`result.json`) and also pushed to Firestore with metadata such as:

- Git branch & commit hash
- Scan timestamp
- LLM issues (if any)
- Bandit warnings

---

## 📊 Example Output (Simplified)

```json
{
  "repo": "AuditAI",
  "branch": "main",
  "commit_hash": "a1b2c3d4",
  "issues": [
    {
      "file": "app/core/auth.py",
      "line": 42,
      "type": "LLM",
      "severity": "HIGH",
      "confidence": "HIGH",
      "description": "Possible hardcoded credentials"
    }
  ]
}
```

---

## 📊 Roadmap

-

---

## 🤝 Contributing

PRs welcome. Please create issues or discussions before major changes.

---

## 🛡️ License

MIT License

---

## 👨‍💻 Maintainer

- **Avinash Karri**\
  [GitHub](https://github.com/Avi2099GIT)

