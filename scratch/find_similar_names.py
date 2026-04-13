import json
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_similar_names():
    with open('subjects.json', 'r') as f:
        data = json.load(f)
    
    subjects_2024 = [s for s in data if s.get('scheme') == 2024 and s.get('dept') == 'CSE']
    
    # Group by sem
    sems = {}
    for s in subjects_2024:
        sem = s.get('sem')
        if sem not in sems:
            sems[sem] = []
        sems[sem].append(s)
    
    for sem, subs in sems.items():
        print(f"\n--- Semester {sem} ---")
        for i in range(len(subs)):
            for j in range(i + 1, len(subs)):
                name1 = subs[i].get('name')
                name2 = subs[j].get('name')
                ratio = similar(name1.lower(), name2.lower())
                if ratio > 0.8:
                    print(f"Similarity {ratio:.2f}:")
                    print(f"  {subs[i]['code']}: {name1}")
                    print(f"  {subs[j]['code']}: {name2}")

if __name__ == "__main__":
    find_similar_names()
