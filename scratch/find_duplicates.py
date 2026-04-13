import json

def analyze_subjects():
    with open('subjects.json', 'r') as f:
        data = json.load(f)
    
    # Filter for 2024 scheme
    subjects_2024 = [s for s in data if s.get('scheme') == 2024]
    
    print(f"Total 2024 subjects: {len(subjects_2024)}")
    
    # Check for duplicates by code
    codes = {}
    for s in subjects_2024:
        key = (s.get('dept'), s.get('sem'), s.get('code'))
        if key in codes:
            codes[key].append(s)
        else:
            codes[key] = [s]
            
    code_dupes = {k: v for k, v in codes.items() if len(v) > 1}
    if code_dupes:
        print("\nDuplicates by CODE (dept, sem, code):")
        for k, v in code_dupes.items():
            print(f"{k}: {len(v)} occurrences")
    else:
        print("\nNo duplicates by code found.")

    # Check for duplicates by name
    names = {}
    for s in subjects_2024:
        key = (s.get('dept'), s.get('sem'), s.get('name'))
        if key in names:
            names[key].append(s)
        else:
            names[key] = [s]
            
    name_dupes = {k: v for k, v in names.items() if len(v) > 1}
    if name_dupes:
        print("\nDuplicates by NAME (dept, sem, name):")
        for k, v in name_dupes.items():
            print(f"{k}: codes: {[s['code'] for s in v]}")
    else:
        print("\nNo duplicates by name found.")

if __name__ == "__main__":
    analyze_subjects()
