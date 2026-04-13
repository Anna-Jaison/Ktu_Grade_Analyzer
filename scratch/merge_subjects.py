import json
import os

# Input string containing multiple JSON arrays
input_str = """
[
  {"sem":8,"code":"PECST86N","name":"Program Elective 6","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":8,"code":"OECST83N","name":"Open Elective 3","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":8,"code":"UEHUT803","name":"Organizational Behavior & Business Communication","credits":2,"internal":50,"external":50},

  {"sem":8,"code":"PCCSP806","name":"Major Project / Internship","credits":4,"internal":100,"external":0}
][
  {"sem":7,"code":"PECST74N","name":"Program Elective 4","credits":3,"elective":true,"internal":40,"external":60},
  {"sem":7,"code":"PECST75N","name":"Program Elective 5","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":7,"code":"OECST72N","name":"Open Elective 2","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":7,"code":"UEHUT704","name":"Humanities Elective","credits":2,"internal":50,"external":50},

  {"sem":7,"code":"PCCSS705","name":"Seminar","credits":2,"internal":50,"external":0},
  {"sem":7,"code":"PCCSP706","name":"Project / Internship","credits":4,"internal":100,"external":0}
][
  {"sem":6,"code":"PCCST601","name":"Compiler Design","credits":4,"internal":40,"external":60},
  {"sem":6,"code":"PCCST602","name":"Advanced Computing Systems","credits":3,"internal":40,"external":60},

  {"sem":6,"code":"PECST63N","name":"Program Elective 3","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":6,"code":"PBCST604","name":"Fundamentals of Cyber Security","credits":4,"internal":60,"external":40},

  {"sem":6,"code":"GAEST605","name":"Design Thinking & Product Development","credits":2,"internal":40,"external":60},

  {"sem":6,"code":"OECST61N","name":"Open Elective 1","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":6,"code":"PCCSL607","name":"Systems Lab","credits":2,"lab":true,"internal":50,"external":50},
  {"sem":6,"code":"PCCSP608","name":"Mini Project","credits":2,"internal":50,"external":50}
][
  {"sem":5,"code":"PCCST501","name":"Computer Networks","credits":4,"internal":40,"external":60},
  {"sem":5,"code":"PCCST502","name":"Design and Analysis of Algorithms","credits":4,"internal":40,"external":60},
  {"sem":5,"code":"PCCST503","name":"Machine Learning","credits":3,"internal":40,"external":60},

  {"sem":5,"code":"PBCST504","name":"Microcontrollers","credits":4,"internal":60,"external":40},

  {"sem":5,"code":"PECST52N","name":"Program Elective 2","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":5,"code":"UCHUM506","name":"Constitution of India (MOOC)","credits":1,"internal":0,"external":0},

  {"sem":5,"code":"PCCSL507","name":"Networks Lab","credits":2,"lab":true,"internal":50,"external":50},
  {"sem":5,"code":"PCCSL508","name":"Machine Learning Lab","credits":2,"lab":true,"internal":50,"external":50}
][
  {"sem":4,"code":"GAMAT401","name":"Mathematics for Information Science-4","credits":3,"internal":40,"external":60},

  {"sem":4,"code":"PCCST402","name":"Database Management Systems","credits":4,"internal":40,"external":60},
  {"sem":4,"code":"PCCST403","name":"Operating Systems","credits":4,"internal":40,"external":60},

  {"sem":4,"code":"PBCST404","name":"Computer Organization & Architecture","credits":4,"internal":60,"external":40},

  {"sem":4,"code":"PECST41N","name":"Program Elective 1","credits":3,"elective":true,"internal":40,"external":60},

  {"sem":4,"code":"UCHUT346","name":"Economics for Engineers","credits":2,"internal":50,"external":50,"group":"S3/S4"},
  {"sem":4,"code":"UCHUT347","name":"Engineering Ethics & Sustainable Development","credits":2,"internal":50,"external":50,"group":"S3/S4"},

  {"sem":4,"code":"PCCSL407","name":"Operating Systems Lab","credits":2,"lab":true,"internal":50,"external":50},
  {"sem":4,"code":"PCCSL408","name":"DBMS Lab","credits":2,"lab":true,"internal":50,"external":50}
][
  {"sem":3,"code":"GAMAT301","name":"Mathematics for Information Science-3","credits":3,"lab":false,"internal":40,"external":60},

  {"sem":3,"code":"PCCST302","name":"Theory of Computation","credits":4,"lab":false,"internal":40,"external":60},
  {"sem":3,"code":"PCCST303","name":"Data Structures and Algorithms","credits":4,"lab":false,"internal":40,"external":60},

  {"sem":3,"code":"PBCST304","name":"Object Oriented Programming","credits":4,"lab":false,"internal":60,"external":40},

  {"sem":3,"code":"GAEST305","name":"Digital Electronics & Logic Design","credits":4,"lab":false,"internal":40,"external":60},

  {"sem":3,"code":"UCHUT346","name":"Economics for Engineers","credits":2,"lab":false,"internal":50,"external":50,"group":"S3/S4"},
  {"sem":3,"code":"UCHUT347","name":"Engineering Ethics & Sustainable Development","credits":2,"lab":false,"internal":50,"external":50,"group":"S3/S4"},

  {"sem":3,"code":"PCCSL307","name":"Data Structures Lab","credits":2,"lab":true,"internal":50,"external":50},
  {"sem":3,"code":"PCCSL308","name":"Digital Lab","credits":2,"lab":true,"internal":50,"external":50}
][
  {"sem":2,"code":"GAMAT201","name":"Mathematics for Information Science-2","credits":3,"type":"BSC","lab":false,"internal":40,"external":60},

  {"sem":2,"code":"GAPHT121","name":"Physics for Information Science","credits":4,"lab":true,"internal":40,"external":60,"group":"S1/S2"},
  {"sem":2,"code":"GXCYT122","name":"Chemistry for Information Science","credits":4,"lab":true,"internal":40,"external":60,"group":"S1/S2"},

  {"sem":2,"code":"GXEST203","name":"Foundations of Computing","credits":3,"lab":false,"internal":40,"external":60},
  {"sem":2,"code":"GXEST204","name":"Programming in C","credits":4,"lab":true,"internal":40,"external":60},

  {"sem":2,"code":"PCCST205","name":"Discrete Mathematics","credits":4,"lab":false,"internal":40,"external":60},

  {"sem":2,"code":"UCEST206","name":"Entrepreneurship & IPR","credits":3,"lab":false,"internal":60,"external":40},

  {"sem":2,"code":"GXESL208","name":"IT Workshop","credits":1,"lab":true,"internal":50,"external":50},

  {"sem":2,"code":"UCSEM129","name":"Digital 101 (MOOC)","credits":1,"lab":false,"internal":0,"external":0}
][
  {"sem":1,"code":"GAMAT101","name":"Mathematics for Information Science-1","credits":3,"type":"BSC","category":"GC","lab":false,"internal":40,"external":60},

  {"sem":1,"code":"GAPHT121","name":"Physics for Information Science","credits":4,"type":"BSC","category":"GC","lab":true,"internal":40,"external":60,"group":"S1/S2"},
  {"sem":1,"code":"GXCYT122","name":"Chemistry for Information Science","credits":4,"type":"BSC","category":"GC","lab":true,"internal":40,"external":60,"group":"S1/S2"},

  {"sem":1,"code":"GMEST103","name":"Engineering Graphics and CAD","credits":3,"type":"ESC","category":"GC","lab":true,"internal":40,"external":60},

  {"sem":1,"code":"GXEST104","name":"Intro to Electrical & Electronics Engineering","credits":4,"type":"ESC","category":"GC","lab":false,"internal":40,"external":60},

  {"sem":1,"code":"UCEST105","name":"Algorithmic Thinking with Python","credits":4,"type":"ESC","category":"UC","lab":true,"internal":40,"external":60},

  {"sem":1,"code":"GXESL106","name":"EEE Workshop","credits":1,"type":"ESC","category":"GC","lab":true,"internal":50,"external":50},

  {"sem":1,"code":"UCHWT127","name":"Health and Wellness","credits":0,"type":"HWP","category":"UC","lab":false,"internal":50,"external":0,"group":"S1/S2"},
  {"sem":1,"code":"UCHUT128","name":"Life Skills & Professional Communication","credits":0,"type":"HMC","category":"UC","lab":false,"internal":100,"external":0,"group":"S1/S2"},

  {"sem":1,"code":"UCSEM129","name":"Digital 101 (MOOC)","credits":1,"type":"SEC","category":"UC","lab":false,"internal":0,"external":0}
]
"""

# Fix the JSON concatenation issue (replace ][ with ],[)
json_str = "[" + input_str.replace("][", "],[") + "]"
# Flatten the nested lists
nested_subjects = json.loads(json_str)
all_new_subjects = [item for sublist in nested_subjects for item in sublist]

filepath = 'subjects.json'
with open(filepath, 'r') as f:
    existing_data = json.load(f)

# Track existing codes for 2024 scheme to prevent duplicates
existing_keys = set()
for s in existing_data:
    if s.get('scheme') == 2024:
        existing_keys.add(s['code'])

count = 0
for sub in all_new_subjects:
    code = sub['code']
    if code in existing_keys:
        # Check if the existing record was partial or needs info update? 
        # For now, let's just skip duplicates or update them.
        # The user said "add this too", which might mean "replace" or "supplement".
        # I'll update the existing one to be sure it has the new info.
        for existing in existing_data:
            if existing.get('scheme') == 2024 and existing['code'] == code:
                # Update fields
                existing['name'] = sub.get('name', existing['name'])
                existing['credits'] = sub.get('credits', existing['credits'])
                existing['max_internal'] = sub.get('internal', existing['max_internal'])
                existing['max_external'] = sub.get('external', existing['max_external'])
                existing['total'] = sub.get('internal', 0) + sub.get('external', 0)
                existing['lab'] = sub.get('lab', existing.get('lab', False))
                # Add any new metadata
                if 'group' in sub: existing['group'] = sub['group']
                if 'type' in sub: existing['type'] = sub['type']
                if 'category' in sub: existing['category'] = sub['category']
                break
        continue
    
    # Map fields
    new_sub = {
        "sem": sub['sem'],
        "code": sub['code'],
        "name": sub['name'],
        "credits": sub['credits'],
        "elective": sub.get('elective', False),
        "lab": sub.get('lab', False),
        "dept": "CSE",  
        "scheme": 2024,
        "max_internal": sub.get('internal', 0),
        "max_external": sub.get('external', 0),
        "total": sub.get('internal', 0) + sub.get('external', 0)
    }
    
    # Optional fields
    if 'group' in sub:
        new_sub['group'] = sub['group']
    if 'type' in sub:
        new_sub['type'] = sub['type']
    if 'category' in sub:
        new_sub['category'] = sub['category']

    existing_data.append(new_sub)
    count += 1

with open(filepath, 'w') as f:
    json.dump(existing_data, f, indent=4)

print(f"Added {count} new subjects and updated duplicates.")
