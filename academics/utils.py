# Grade maps
# 2019 Scheme: Passing Total 75/150 (50%)
GRADE_MAP = {
    "S": (90, 10),
    "A+": (85, 9),
    "A": (80, 8.5),
    "B+": (75, 8),
    "B": (70, 7.5),
    "C+": (65, 7),
    "C": (60, 6.5),
    "D": (50, 6),
    "P": (40, 5.5),
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


def get_mark_limits(is_lab=False, scheme=2019):
    if scheme == 2024:
        if is_lab:
            return {"max_internal": 50, "max_external": 50}
        return {"max_internal" , "max_external"}

    if is_lab:
        return {"max_internal": 75, "max_external": 75}

    return {"max_internal": 50, "max_external": 100}


def required_external_for_total(internal, target_total, max_external, scheme=2019):
    required = target_total - internal

    # Minimum ESE threshold (40%)
    if scheme == 2024:
        ese_min = round(max_external * 0.40, 2)
    else:
        ese_min = round(max_external * 0.35, 2)

    if required <= 0:
        return ese_min
        
    if required > max_external:
        return "Not Possible"

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
    ese_min = round(max_external * 0.40, 2)

    if scheme == 2024:
        return external >= ese_min and total >= 50

    # 2019 logic: ESE min 40%, Total min 50%
    # Pass threshold is 50% of (max_internal + max_external), but for 150 marks it's often set to 75.
    pass_total = 40 if scheme == 2019 else 50
    
    return external >= ese_min and total >= pass_total
