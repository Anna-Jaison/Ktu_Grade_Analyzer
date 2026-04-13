# Grade maps
# 2019 Scheme: Passing Total 75/150 (50%)
GRADE_MAP = {
    "S": (135, 10),
    "A+": (128, 9),
    "A": (120, 8.5),
    "B+": (113, 8),
    "B": (105, 7.5),
    "C+": (98, 7),
    "C": (90, 6.5),
    "D": (83, 6),
    "P": (75, 5.5),
}

# 2024 Scheme: Passing Total 50/100 (50%)
GRADE_MAP_2024 = {
    "S": (90, 10),
    "A+": (85, 9),
    "A": (80, 8.5),
    "B+": (75, 8),
    "B": (70, 7.5),
    "C+": (65, 7),
    "C": (60, 6.5),
    "D": (55, 6),
    "P": (50, 5.5),
}


def get_grade_map(scheme):
    return GRADE_MAP_2024 if scheme == 2024 else GRADE_MAP


def get_pass_mark_total(scheme):
    return 50 if scheme == 2024 else 75




def required_external_for_total(internal, target_total, max_external, scheme=2019):
    required = target_total - internal

    ese_min = round(max_external * (0.40 if scheme == 2024 else 0.35), 2)

    # ✅ If already enough internal
    if required <= 0:
        return ese_min

    # ✅ If impossible
    if required > max_external:
        return "Not Possible"

    # ✅ Final required
    return max(ese_min, round(required, 2))


def get_required_externals_by_grade(internal, max_external, scheme=2019):
    result = {}
    grade_map = get_grade_map(scheme)

    for grade, (min_total, _) in grade_map.items():
        required = required_external_for_total(
            internal, min_total, max_external, scheme
        )
        result[grade] = required

    return result


def get_grade(total, scheme=2019):
    grade_map = get_grade_map(scheme)

    for grade, (min_mark, _) in grade_map.items():
        if total >= min_mark:
            return grade
    return "F"


def get_grade_point(grade, scheme=2019):
    grade_map = get_grade_map(scheme)
    return grade_map.get(grade, (0, 0))[1]

def is_pass(internal, external, max_internal, max_external, scheme=2019):
    total = internal + external
    ese_min = round(max_external * (0.40 if scheme == 2024 else 0.35), 2)

    # 2019 logic: ESE min 40%, Total min 50%
    # Pass threshold is 50% of (max_internal + max_external), but for 150 marks it's often set to 75.
    pass_total = 75 if scheme == 2019 else 50
    
    return external >= ese_min and total >= pass_total
