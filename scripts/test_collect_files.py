from app.scanner.collector import collect_python_files

if __name__ == "__main__":
    path = "."  # or specific path to your source folder
    files = collect_python_files(path)
    print(f"Found {len(files)} Python files:")
    for f in files:
        print(" -", f)