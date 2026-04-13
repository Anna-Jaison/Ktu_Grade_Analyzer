import json

def reconstruct_extract_subject():
    # Load the cleaned subjects.json
    with open('subjects.json', 'r', encoding='utf-8') as f:
        subjects = json.load(f)
    
    # Sort subjects for better readability in the script
    # Sort by scheme, then dept, then sem, then code
    subjects.sort(key=lambda x: (x.get('scheme', 2019), x.get('dept', 'CSE'), x['sem'], x['code']))
    
    header = """import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ktu_grade_analyzer.settings")
django.setup()

from academics.models import *

# ✅ CLEANED DATA (FROM subjects.json)
DATA = [
"""
    
    footer = """
]

def insert_data():
    for item in DATA:
        try:
            # Get scheme year from data, default to 2019
            scheme_year = item.get("scheme", 2019)
            scheme = Scheme.objects.get(year=scheme_year)
            
            dept_name = item.get("dept", "CSE")
            dept = Department.objects.get(name=dept_name)

            semester = Semester.objects.get(number=item["sem"], scheme=scheme)

            obj, created = Subject.objects.update_or_create(
                code=item["code"],
                defaults={
                    "name": item["name"],
                    "credits": item["credits"],
                    "department": dept,
                    "semester": semester,
                    "is_elective": item.get("elective", item.get("is_elective", False)),
                    "is_lab": item.get("lab", item.get("is_lab", False))
                }
            )

            if created:
                print(f"✅ Added: {item['code']} (Scheme {scheme_year})")
            else:
                # print(f"♻️ Updated: {item['code']} (Scheme {scheme_year})")
                pass

        except Exception as e:
            print(f"❌ Error with {item['code']} -> {e}")

    print("🔥 DONE - Database synchronized with subjects.json")


if __name__ == "__main__":
    insert_data()
"""

    lines = []
    current_scheme = None
    current_dept = None
    
    for s in subjects:
        scheme = s.get('scheme', 2019)
        dept = s.get('dept', 'CSE')
        
        if scheme != current_scheme or dept != current_dept:
            lines.append(f"\n    # ---------- {dept} Scheme {scheme} ----------")
            current_scheme = scheme
            current_dept = dept
        
        # Format the dict slightly nicer for the file
        # Ensure it has 'elective' and 'lab' keys instead of 'is_elective' if possible
        # but the model update logic handles both.
        
        # We'll normalize to the structure used by the script
        normalized = {
            "sem": s["sem"],
            "code": s["code"],
            "name": s["name"],
            "credits": s["credits"],
            "elective": s.get("elective", s.get("is_elective", False)),
            "lab": s.get("lab", s.get("is_lab", False)),
            "dept": dept,
            "scheme": scheme
        }
        lines.append(f"    {repr(normalized)},")
        
    with open('extract_subject.py', 'w', encoding='utf-8') as f:
        f.write(header)
        f.write("\n".join(lines))
        f.write(footer)
    
    print("✅ extract_subject.py has been reconstructed from subjects.json.")

if __name__ == "__main__":
    reconstruct_extract_subject()
