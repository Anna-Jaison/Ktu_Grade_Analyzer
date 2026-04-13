import sys
import os

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ktu_grade_analyzer.settings')
import django
django.setup()

from academics.utils import required_external_for_total, is_pass

print("--- 2024 DYNAMIC Scheme subjects ---")

# Microcontrollers (60/40)
# Pass: Total 50, ESE 16 (40% of 40)
print(f"Microcontrollers (60/40): Int 30, Target 50: {required_external_for_total(30, 50, 40, scheme=2024)} (Expected: 20)")
print(f"Microcontrollers (60/40): Int 40, Target 50: {required_external_for_total(40, 50, 40, scheme=2024)} (Expected: 16 - ESE min 16)")

# Life Skills (100/0)
# Pass: Total 50, ESE 0
print(f"Life Skills (100/0): Int 40, Target 50: {required_external_for_total(40, 50, 0, scheme=2024)} (Expected: 10)")
print(f"Life Skills (100/0): Int 60, Target 50: {required_external_for_total(60, 50, 0, scheme=2024)} (Expected: 0)")

# Compiler Design (40/60)
# Pass: Total 50, ESE 24
print(f"Compiler Design (40/60): Int 26, Target 50: {required_external_for_total(26, 50, 60, scheme=2024)} (Expected: 24)")

print("\n--- is_pass check ---")
# is_pass(internal, external, max_internal, max_external, scheme)
print(f"Micro: Int 40, Ext 15 -> {is_pass(40, 15, 60, 40, 2024)} (Expected: False - ESE min 16)")
print(f"Micro: Int 40, Ext 16 -> {is_pass(40, 16, 60, 40, 2024)} (Expected: True - Total 56, ESE 16)")
print(f"Life: Int 40, Ext 0 -> {is_pass(40, 0, 100, 0, 2024)} (Expected: False - Total 40)")
print(f"Life: Int 50, Ext 0 -> {is_pass(50, 0, 100, 0, 2024)} (Expected: True - Total 50)")

print("\n--- 2019 Scheme Consistency ---")
# 2019 Theory (50/100)
# Pass: Total 75, ESE 40
print(f"2019 Theory: Int 30, Target 75: {required_external_for_total(30, 75, 100, scheme=2019)} (Expected: 45)")
print(f"2019 Theory: Int 40, Target 75: {required_external_for_total(40, 75, 100, scheme=2019)} (Expected: 40 - ESE min 40)")
