# app/utils/code_utils.py

import ast

def extract_code_blocks(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    blocks = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            block_code = ast.get_source_segment(source, node)
            blocks.append({
                "line_number": node.lineno,
                "code": block_code
            })

    return blocks
