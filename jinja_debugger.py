import re
from pathlib import Path
from docx import Document

# 🛠️ Hardcode your template path here (absolute or relative)
template_file = r"/Users/p-jack-l/Downloads/SingleEP_jinja_template.docx"  # or .txt, .jinja, etc.

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_jinja_blocks(text):
    patterns = {
        "variables": r"{{\s*([a-zA-Z_][\w]*(?:\[[^\]]+\]|\.[a-zA-Z_][\w]*)*)\s*}}",
        "if": r"{%\s*if\s+([^%]+?)\s*%}",
        "elif": r"{%\s*elif\s+([^%]+?)\s*%}",
        "else": r"{%\s*else\s*%}",
        "endif": r"{%\s*endif\s*%}",
        "for": r"{%\s*for\s+.+?\s+in\s+(.+?)\s*%}",
        "endfor": r"{%\s*endfor\s*%}"
    }

    results = []
    for block_type, pattern in patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            results.append((block_type.upper(), match.strip()))
    return results

def debug_template(file_path):
    ext = Path(file_path).suffix.lower()

    if ext == ".docx":
        content = extract_text_from_docx(file_path)
    else:
        content = Path(file_path).read_text(encoding="utf-8")

    blocks = extract_jinja_blocks(content)

    if not blocks:
        print("⚠️ No Jinja2 syntax found.")
    else:
        print(f"\n🔍 Jinja2 Blocks Found in {file_path}:\n")
        for block_type, expression in blocks:
            print(f"[{block_type}]  {expression}")

# Run the debugger if the file exists
if Path(template_file).exists():
    debug_template(template_file)
else:
    print(f"❌ File not found: {template_file}")
