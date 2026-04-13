import sys
import os

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ktu_grade_analyzer.settings')
import django
django.setup()

from academics.utils import required_external_for_total, is_pass

print("--- REVISED 2019 Scheme Theory ---")
# 2019 Theory: Max 150 (50+100)
# Pass: Total 75, ESE 40
print(f"Internal 35, Target 75: {required_external_for_total(35, 75, is_lab=False, scheme=2019)} (Expected: 40)")
print(f"Internal 40, Target 75: {required_external_for_total(40, 75, is_lab=False, scheme=2019)} (Expected: 40 - ESE min 40)")
print(f"Internal 0, Target 75: {required_external_for_total(0, 75, is_lab=False, scheme=2019)} (Expected: 75)")

print("\n--- REVISED 2019 Scheme Lab ---")
# 2019 Lab: Max 150 (75+75)
# Pass: Total 75, ESE 30 (40% of 75)
print(f"Internal 40, Target 75: {required_external_for_total(40, 75, is_lab=True, scheme=2019)} (Expected: 35)")
print(f"Internal 50, Target 75: {required_external_for_total(50, 75, is_lab=True, scheme=2019)} (Expected: 30 - ESE min 30)")

print("\n--- REVISED 2024 Scheme ---")
# 2024: Max 100 (40+60)
# Pass: Total 50, ESE 24
print(f"Internal 26, Target 50: {required_external_for_total(26, 50, scheme=2024)} (Expected: 24)")
print(f"Internal 30, Target 50: {required_external_for_total(30, 50, scheme=2024)} (Expected: 24)")

print("\n--- is_pass check ---")
print(f"2019: Int 35, Ext 40 -> {is_pass(35, 40, 2019)} (Expected: True)")
print(f"2019: Int 40, Ext 35 -> {is_pass(40, 35, 2019)} (Expected: False - ESE min 40)")
print(f"2024: Int 26, Ext 24 -> {is_pass(26, 24, 2024)} (Expected: True)")
print(f"2024: Int 30, Ext 20 -> {is_pass(30, 20, 2024)} (Expected: False - ESE 20 < 24)")
