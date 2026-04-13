import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ktu_grade_analyzer.settings")
django.setup()

from academics.models import *

# ✅ CLEANED DATA (FROM subjects.json)
DATA = [

    # ---------- CSE Scheme 2019 ----------
    {'sem': 1, 'code': 'ESL130', 'name': 'Electrical and Electronics Workshop', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 1, 'code': 'EST100', 'name': 'Engineering Mechanics', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 1, 'code': 'EST130', 'name': 'Basics of Electrical and Electronics Engineering', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 1, 'code': 'HUN101', 'name': 'Life Skills', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 1, 'code': 'MAT101', 'name': 'Linear Algebra and Calculus', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 1, 'code': 'PHL120', 'name': 'Engineering Physics Lab', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 1, 'code': 'PHT100', 'name': 'Engineering Physics A', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'CYL120', 'name': 'Engineering Chemistry Lab', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'CYT100', 'name': 'Engineering Chemistry', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'ESL120', 'name': 'Civil and Mechanical Workshop', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST102', 'name': 'Programming in C', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST110', 'name': 'Engineering Graphics', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST120', 'name': 'Basics of Civil and Mechanical Engineering', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'HUN102', 'name': 'Professional Communication', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 2, 'code': 'MAT102', 'name': 'Vector Calculus, Differential Equations and Transforms', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'CSL201', 'name': 'Data Structures Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'CSL203', 'name': 'Object Oriented Programming Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'CST201', 'name': 'Data Structures', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'CST203', 'name': 'Logic System Design', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'CST205', 'name': 'Object Oriented Programming using Java', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'HUT200', 'name': 'Professional Ethics', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'MAT203', 'name': 'Discrete Mathematical Structures', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 3, 'code': 'MCN201', 'name': 'Sustainable Engineering', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'CSL202', 'name': 'Digital Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'CSL204', 'name': 'Operating Systems Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'CST202', 'name': 'Computer Organisation and Architecture', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'CST204', 'name': 'Database Management Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'CST206', 'name': 'Operating Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'EST200', 'name': 'Design and Engineering', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'MAT206', 'name': 'Graph Theory', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 4, 'code': 'MCN202', 'name': 'Constitution of India', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CSL331', 'name': 'System Software and Microprocessors Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CSL333', 'name': 'Database Management Systems Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CST301', 'name': 'Formal Languages and Automata Theory', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CST303', 'name': 'Computer Networks', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CST305', 'name': 'System Software', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CST307', 'name': 'Microprocessors and Microcontrollers', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'CST309', 'name': 'Management of Software Systems', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 5, 'code': 'MCN301', 'name': 'Disaster Management', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'CSD334', 'name': 'Mini Project', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'CSL332', 'name': 'Networking Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'CST302', 'name': 'Compiler Design', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'CST304', 'name': 'Computer Graphics and Image Processing', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'CST306', 'name': 'Algorithm Analysis and Design', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'CST362', 'name': 'Programming in Python', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 6, 'code': 'HUT300', 'name': 'Industrial Economics and Foreign Trade', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'CSD415', 'name': 'Project Phase I', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'CSL411', 'name': 'Compiler Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'CSQ413', 'name': 'Seminar', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'CST401', 'name': 'Artificial Intelligence', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'CST463', 'name': 'Web Programming', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'EET455', 'name': 'Energy Management', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 7, 'code': 'MCN401', 'name': 'Industrial Safety Engineering', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 8, 'code': 'CSD416', 'name': 'Project Phase II', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 8, 'code': 'CST408', 'name': 'Comprehensive Exam', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 8, 'code': 'CST441', 'name': 'Elective III', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 8, 'code': 'CST443', 'name': 'Elective V', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 8, 'code': 'CST445', 'name': 'Elective IV', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'CSE', 'scheme': 2019},
    {'sem': 8, 'code': 'CST450', 'name': 'Distributed Computing', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'CSE', 'scheme': 2019},

    # ---------- ECE Scheme 2019 ----------
    {'sem': 1, 'code': 'ESL130', 'name': 'Electrical and Electronics Workshop', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 1, 'code': 'EST100', 'name': 'Engineering Mechanics', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 1, 'code': 'EST130', 'name': 'Basics of Electrical and Electronics Engineering', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 1, 'code': 'HUN101', 'name': 'Life Skills', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 1, 'code': 'MAT101', 'name': 'Linear Algebra and Calculus', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 1, 'code': 'PHL120', 'name': 'Engineering Physics Lab', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 1, 'code': 'PHT100', 'name': 'Engineering Physics A', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'CYL120', 'name': 'Engineering Chemistry Lab', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'CYT100', 'name': 'Engineering Chemistry', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'ESL120', 'name': 'Civil and Mechanical Workshop', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST102', 'name': 'Programming in C', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST110', 'name': 'Engineering Graphics', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST120', 'name': 'Basics of Civil and Mechanical Engineering', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'HUN102', 'name': 'Professional Communication', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 2, 'code': 'MAT102', 'name': 'Vector Calculus, Differential Equations and Transforms', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 3, 'code': 'ECL201', 'name': 'Electronic Devices Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 3, 'code': 'ECL203', 'name': 'Network Theory Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 3, 'code': 'ECT201', 'name': 'Signals and Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 3, 'code': 'ECT203', 'name': 'Electronic Devices', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 3, 'code': 'ECT205', 'name': 'Network Theory', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 4, 'code': 'ECL202', 'name': 'Analog Circuits Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 4, 'code': 'ECL204', 'name': 'Digital Electronics Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 4, 'code': 'ECT202', 'name': 'Analog Electronic Circuits', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 4, 'code': 'ECT204', 'name': 'Digital Electronics', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 4, 'code': 'ECT206', 'name': 'Electromagnetic Theory', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECL331', 'name': 'IC Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECL333', 'name': 'Microcontroller Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECT301', 'name': 'Linear Integrated Circuits', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECT303', 'name': 'Microprocessors and Microcontrollers', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECT305', 'name': 'Analog Communication', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECT307', 'name': 'Control Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 5, 'code': 'ECT309', 'name': 'Digital Signal Processing', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECL332', 'name': 'Communication Systems Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECL334', 'name': 'Mini Project', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECT302', 'name': 'Digital Communication', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECT304', 'name': 'VLSI', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECT306', 'name': 'Embedded Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECT308', 'name': 'Antenna and Wave Propagation', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 6, 'code': 'ECT362', 'name': 'Open Elective', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECD415', 'name': 'Project Phase I', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECL411', 'name': 'Communication Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECQ413', 'name': 'Seminar', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECT401', 'name': 'Microwave and Radar Engineering', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECT403', 'name': 'DSP Applications', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECT405', 'name': 'Computer Communication', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECT407', 'name': 'Elective I', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 7, 'code': 'ECT409', 'name': 'Elective II', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 8, 'code': 'ECD416', 'name': 'Project Phase II', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 8, 'code': 'ECT402', 'name': 'Elective III', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 8, 'code': 'ECT404', 'name': 'Elective IV', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 8, 'code': 'ECT406', 'name': 'Elective V', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'ECE', 'scheme': 2019},
    {'sem': 8, 'code': 'ECT408', 'name': 'Comprehensive Exam', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'ECE', 'scheme': 2019},

    # ---------- EEE Scheme 2019 ----------
    {'sem': 1, 'code': 'ESL130', 'name': 'Electrical Workshop', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 1, 'code': 'EST100', 'name': 'Engineering Mechanics', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 1, 'code': 'EST130', 'name': 'Basics of Electrical and Electronics Engineering', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 1, 'code': 'HUN101', 'name': 'Life Skills', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 1, 'code': 'MAT101', 'name': 'Linear Algebra and Calculus', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 1, 'code': 'PHL120', 'name': 'Engineering Physics Lab', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 1, 'code': 'PHT100', 'name': 'Engineering Physics A', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'CYL120', 'name': 'Engineering Chemistry Lab', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'CYT100', 'name': 'Engineering Chemistry', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'ESL120', 'name': 'Workshop', 'credits': 1, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST102', 'name': 'Programming in C', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST110', 'name': 'Engineering Graphics', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'EST120', 'name': 'Basics of Civil and Mechanical Engineering', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'HUN102', 'name': 'Professional Communication', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 2, 'code': 'MAT102', 'name': 'Vector Calculus, Differential Equations and Transforms', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'EEL201', 'name': 'Circuits Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'EEL203', 'name': 'Analog Electronics Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'EET201', 'name': 'Circuits and Networks', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'EET203', 'name': 'Analog Electronics', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'EET205', 'name': 'Electrical Measurements and Instrumentation', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'HUT200', 'name': 'Professional Ethics', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'MAT203', 'name': 'Discrete Mathematical Structures', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 3, 'code': 'MCN201', 'name': 'Sustainable Engineering', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'EEL202', 'name': 'Electrical Machines Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'EEL204', 'name': 'Digital Electronics Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'EET202', 'name': 'DC Machines and Transformers', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'EET204', 'name': 'Digital Electronics', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'EET206', 'name': 'Electromagnetic Theory', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'EST200', 'name': 'Design and Engineering', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'MAT208', 'name': 'Transforms and Partial Differential Equations', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 4, 'code': 'MCN202', 'name': 'Constitution of India', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EEL331', 'name': 'Power Electronics Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EEL333', 'name': 'Microcontroller Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EET301', 'name': 'Power Systems I', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EET303', 'name': 'Power Electronics', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EET305', 'name': 'Control Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EET307', 'name': 'Electrical Machines', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'EET309', 'name': 'Microprocessors and Microcontrollers', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 5, 'code': 'MCN301', 'name': 'Disaster Management', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EEL332', 'name': 'Drives Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EEL334', 'name': 'Mini Project', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EET302', 'name': 'Power Systems II', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EET304', 'name': 'Electric Drives', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EET306', 'name': 'Renewable Energy Systems', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EET308', 'name': 'High Voltage Engineering', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'EET362', 'name': 'Open Elective', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 6, 'code': 'HUT300', 'name': 'Industrial Economics and Foreign Trade', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EED415', 'name': 'Project Phase I', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EEL411', 'name': 'Power Systems Lab', 'credits': 2, 'elective': False, 'lab': True, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EEQ413', 'name': 'Seminar', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EET401', 'name': 'Power System Protection', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EET403', 'name': 'Smart Grid', 'credits': 3, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EET405', 'name': 'Elective I', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'EET407', 'name': 'Elective II', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 7, 'code': 'MCN401', 'name': 'Industrial Safety Engineering', 'credits': 0, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 8, 'code': 'EED416', 'name': 'Project Phase II', 'credits': 4, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 8, 'code': 'EET402', 'name': 'Elective III', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 8, 'code': 'EET404', 'name': 'Elective IV', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 8, 'code': 'EET406', 'name': 'Elective V', 'credits': 3, 'elective': True, 'lab': False, 'dept': 'EEE', 'scheme': 2019},
    {'sem': 8, 'code': 'EET408', 'name': 'Comprehensive Exam', 'credits': 2, 'elective': False, 'lab': False, 'dept': 'EEE', 'scheme': 2019},

    # ---------- CSE Scheme 2024 ----------
    
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
                semester=semester,
                defaults={
                    "name": item["name"],
                    "credits": item["credits"],
                    "department": dept,
                    "is_elective": item.get("elective", item.get("is_elective", False)),
                    "is_lab": item.get("lab", item.get("is_lab", False))
                }
            )

            if created:
                print(f"Added: {item['code']} (Scheme {scheme_year})")

        except Exception as e:
            print(f"Error with {item['code']} -> {e}")

    print("DONE - Database synchronized with subjects.json")


if __name__ == "__main__":
    insert_data()
