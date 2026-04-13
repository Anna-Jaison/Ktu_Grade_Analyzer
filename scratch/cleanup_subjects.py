import json
import os

def cleanup_subjects():
    file_path = 'subjects.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # List of codes to REMOVE for 2024 CSE
    to_remove = [
        # Sem 4
        "PCCST404", # Redundant DBMS
        "PCCST405", # OS Lab 1cr (keep PCCSL407 2cr)
        "PCCST406", # DBMS Lab 1cr (keep PCCSL408 2cr)
        
        # Redundant Electives (Standardizing on Roman Numerals PEC/OEC where both exist)
        "PECST52N", 
        "PECST63N",
        "PECST74N",
        "PECST75N",
        "PECST86N",
        "OECST61N",
        "OECST72N",
        
        # Redundant Projects/Seminars
        "PCCSS705", # Seminar (keep PWS701)
        "PCCSP706", # Project I (keep PBL701)
        "PCCSP806", # Project II (keep PBL801)
    ]
    
    initial_count = len(data)
    
    # Filter out entries that match the criteria (dept:CSE, scheme:2024, code in to_remove)
    new_data = [
        s for s in data 
        if not (s.get('dept') == 'CSE' and s.get('scheme') == 2024 and s.get('code') in to_remove)
    ]
    
    final_count = len(new_data)
    removed_count = initial_count - final_count
    
    with open(file_path, 'w') as f:
        json.dump(new_data, f, indent=4)
    
    print(f"Removed {removed_count} duplicate subjects.")
    print(f"Final subject count: {final_count}")

if __name__ == "__main__":
    cleanup_subjects()
