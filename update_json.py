import json

with open("subjects.json", "r") as f:
    data = json.load(f)

for sub in data:
    scheme = sub.get("scheme", 2019)

    if scheme == 2024:
        sub["max_internal"] = 40
        sub["max_external"] = 60
        sub["total"] = 100
    else:
        if sub.get("lab"):
            sub["max_internal"] = 75
            sub["max_external"] = 75
        else:
            sub["max_internal"] = 50
            sub["max_external"] = 100
        sub["total"] = 150

with open("subjects_updated.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Updated JSON created")