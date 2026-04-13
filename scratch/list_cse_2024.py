import json

def list_2024_cse():
    with open('subjects.json', 'r') as f:
        data = json.load(f)
    
    cse_2024 = [s for s in data if s.get('scheme') == 2024 and s.get('dept') == 'CSE']
    
    # Sort by sem and name
    cse_2024.sort(key=lambda x: (x.get('sem'), x.get('name')))
    
    for s in cse_2024:
        print(f"Sem: {s.get('sem')}, Code: {s.get('code')}, Name: {s.get('name')}, Credits: {s.get('credits')}, Lab: {s.get('lab')}")

if __name__ == "__main__":
    list_2024_cse()
