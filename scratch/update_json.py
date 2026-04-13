import json
import os

filepath = 'subjects.json'
with open(filepath, 'r') as f:
    data = json.load(f)

count = 0
for sub in data:
    if sub.get('scheme') == 2024 and sub.get('lab') == True:
        sub['max_internal'] = 50
        sub['max_external'] = 50
        count += 1

with open(filepath, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Updated {count} lab subjects in 2024 scheme.")
