import re

def fix_extract_subject():
    with open('extract_subject.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The issue is likely that the 2024 section was pasted as a nested list or has extra brackets.
    # Looking at the previous views, DATA = [ ... ] was the structure.
    # I'll try to flatten it if it's nested.
    
    # More simply, I'll just look for situations where a list is closed and then another bracket is closed.
    # Or just use the fact that len(DATA) == 1 and DATA[0] is a list.
    
    # I'll rewrite the DATA part of the file.
    # I'll extract all dicts from the file and rebuild the DATA list.
    
    dicts = re.findall(r'\{[^{}]+\}', content)
    
    new_data_lines = ["DATA = ["]
    for d in dicts:
        new_data_lines.append(f"    {d},")
    new_data_lines.append("]")
    
    new_data_str = "\n".join(new_data_lines)
    
    # Replace the old DATA assignment with the new one.
    # The old DATA starts at line 10 and ends before insert_data().
    
    start_marker = "# ✅ FIXED DATA"
    end_marker = "def insert_data():"
    
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        new_content = content[:start_index + len(start_marker)] + "\n" + new_data_str + "\n\n\n" + content[end_index:]
        with open('extract_subject.py', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ Fixed extract_subject.py structure.")
    else:
        print("❌ Could not find markers in extract_subject.py.")

if __name__ == "__main__":
    fix_extract_subject()
