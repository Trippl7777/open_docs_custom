import zipfile
import re
from pathlib import Path

def extract_docx_xml(docx_path):
    with zipfile.ZipFile(docx_path, 'r') as z:
        with z.open("word/document.xml") as f:
            return f.read().decode("utf-8")

def check_jinja_blocks(xml_content):
    errors = []
    lines = xml_content.splitlines()
    stack = []

    for i, line in enumerate(lines, 1):
        if "{%" in line or "{{" in line:
            # Check for unclosed blocks
            if "{%" in line and "%}" not in line:
                errors.append(f"Line {i}: Missing '%}}' in control block → {line.strip()}")
            if "{{" in line and "}}" not in line:
                errors.append(f"Line {i}: Missing '}}' in variable block → {line.strip()}")
            if "“" in line or "”" in line or "‘" in line or "’" in line:
                errors.append(f"Line {i}: Contains curly quotes → {line.strip()}")

        # Detect logic blocks
        matches = re.findall(r"{%\s*(\w+)", line)
        for tag in matches:
            if tag in ["if", "for"]:
                stack.append((tag, i))
            elif tag == "endif":
                if not stack or stack[-1][0] != "if":
                    errors.append(f"Line {i}: 'endif' without matching 'if'")
                else:
                    stack.pop()
            elif tag == "endfor":
                if not stack or stack[-1][0] != "for":
                    errors.append(f"Line {i}: 'endfor' without matching 'for'")
                else:
                    stack.pop()

    # Leftover open blocks
    for tag, line_no in stack:
        errors.append(f"Line {line_no}: Unclosed '{tag}' block")

    return errors

if __name__ == "__main__":
    path_to_docx = r"/Users/p-jack-l/Downloads/SingleEP_jinja_template.docx"  # <-- Replace with your path
    xml = extract_docx_xml(path_to_docx)
    issues = check_jinja_blocks(xml)

    if not issues:
        print("✅ No Jinja syntax issues found.")
    else:
        print("❌ Jinja Issues Found:")
        for issue in issues:
            print(" -", issue)
