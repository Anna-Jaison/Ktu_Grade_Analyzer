import json

def analyze_all_2024():
    with open('subjects.json', 'r') as f:
        data = json.load(f)
    
    subjects_2024 = [s for s in data if s.get('scheme') == 2024]
    
    depts = set(s.get('dept') for s in subjects_2024)
    
    for dept in depts:
        print(f"\n--- Department: {dept} ---")
        dept_2024 = [s for s in subjects_2024 if s.get('dept') == dept]
        
        # Duplicates by Name
        names = {}
        for s in dept_2024:
            key = (s.get('sem'), s.get('name'))
            if key in names:
                names[key].append(s)
            else:
                names[key] = [s]
        
        dupes = {k: v for k, v in names.items() if len(v) > 1}
        if dupes:
            for k, v in dupes.items():
                print(f"Sem {k[0]} Duplicate Name: '{k[1]}'")
                for s in v:
                    print(f"  Code: {s['code']}, Credits: {s['credits']}, Lab: {s['lab']}")
        else:
            print("No duplicates by name.")

if __name__ == "__main__":
    analyze_all_2024()
