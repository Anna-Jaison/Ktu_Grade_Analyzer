import json
from collections import defaultdict

def check_duplicates():
    with open('subjects.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    subjects_2024 = [s for s in data if s.get('scheme') == 2024]
    
    # 1. Exact duplicates (code + semester)
    code_sem = defaultdict(list)
    for s in subjects_2024:
        code_sem[(s['code'], s['sem'])].append(s)
    
    print("--- 1. Duplicates (Same Code in Same Semester) ---")
    found_1 = False
    for key, items in code_sem.items():
        if len(items) > 1:
            print(f"Code: {key[0]}, Sem: {key[1]} - Found {len(items)} times")
            found_1 = True
    if not found_1: print("None")
    
    # 2. Name duplicates in same semester
    name_sem = defaultdict(list)
    for s in subjects_2024:
        name_sem[(s['name'], s['sem'])].append(s)
        
    print("\n--- 2. Duplicates (Same Name in Same Semester) ---")
    found_2 = False
    for key, items in name_sem.items():
        if len(items) > 1:
            print(f"Name: {key[0]}, Sem: {key[1]} - Found {len(items)} times: {[s['code'] for s in items]}")
            found_2 = True
    if not found_2: print("None")

    # 3. Code duplicates across DIFFERENT semesters
    code_global = defaultdict(list)
    for s in subjects_2024:
        code_global[s['code']].append(s)
        
    print("\n--- 3. Same Code in Multiple Semesters ---")
    for key, items in code_global.items():
        if len(items) > 1:
            sems = [s['sem'] for s in items]
            print(f"Code: {key} - Found in semesters: {sems}")

if __name__ == "__main__":
    check_duplicates()
