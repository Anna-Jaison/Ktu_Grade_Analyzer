import json
from collections import defaultdict

def check_exact_duplicates():
    with open('subjects.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Group by (dept, sem, scheme) - exactly what the view filters on
    groups = defaultdict(list)
    for s in data:
        key = (s.get('dept', 'CSE'), s['sem'], s.get('scheme', 2019))
        groups[key].append(s)
    
    print("=== Checking each (dept, sem, scheme) group for duplicate codes ===\n")
    found_any = False
    for (dept, sem, scheme), subjects in sorted(groups.items()):
        codes = [s['code'] for s in subjects]
        seen = set()
        dupes = []
        for code in codes:
            if code in seen:
                dupes.append(code)
            seen.add(code)
        
        if dupes:
            found_any = True
            print(f"DUPLICATE in {dept} S{sem} {scheme}: {dupes}")
            for s in subjects:
                if s['code'] in dupes:
                    print(f"  -> {s}")
    
    if not found_any:
        print("No exact duplicates found in any (dept, sem, scheme) group.")
    
    print("\n=== Subject count per (dept, sem, scheme) ===")
    for (dept, sem, scheme), subjects in sorted(groups.items()):
        print(f"  {dept} S{sem} {scheme}: {len(subjects)} subjects")

if __name__ == "__main__":
    check_exact_duplicates()
