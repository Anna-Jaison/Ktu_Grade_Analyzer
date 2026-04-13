import json

def generate_extract_data():
    with open('subjects.json', 'r') as f:
        data = json.load(f)
    
    d2024 = [s for s in data if s.get('scheme') == 2024 and s.get('dept') == 'CSE']
    
    # Sort by sem then code
    d2024.sort(key=lambda x: (x.get('sem'), x.get('code')))
    
    lines = []
    current_sem = None
    for s in d2024:
        if s.get('sem') != current_sem:
            current_sem = s.get('sem')
            lines.append(f"\n    # ---------- CSE 2024 SCHEME SEM {current_sem} ----------")
        
        # Mapping subjects.json fields to extract_subject.py fields
        # Note: some fields like max_internal etc. are not in the extract_subject.py DATA list but handled by defaults?
        # Actually extract_subject.py doesn't use max_internal etc in DATA.
        
        entry = {
            "sem": s.get("sem"),
            "code": s.get("code"),
            "name": s.get("name"),
            "credits": s.get("credits"),
            "elective": s.get("elective", False),
            "lab": s.get("lab", False),
            "dept": "CSE",
            "scheme": 2024
        }
        
        line = f"    {repr(entry).replace('True', 'True').replace('False', 'False')},"
        lines.append(line)
        
    with open('scratch/new_2024_data.txt', 'w') as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    generate_extract_data()
