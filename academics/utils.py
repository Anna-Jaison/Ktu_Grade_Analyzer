# Grade → (minimum total out of 150, grade point)
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

PASS_MARK_TOTAL = 75  # out of 150


def get_mark_limits(is_lab=False):
    if is_lab:
        return {
            "max_internal": 75,
            "max_external": 75,
        }
    return {
        "max_internal": 50,
        "max_external": 100,
    }


def required_external_for_total(internal, target_total, is_lab=False):
    limits = get_mark_limits(is_lab)

    required = target_total - internal

    if required <= 0:
        return 0
    if required > limits["max_external"]:
        return "Not Possible"

    return round(required, 2)


def get_required_externals_by_grade(internal, is_lab=False):
    result = {}
    for grade, (min_total, _) in GRADE_MAP.items():
        result[grade] = required_external_for_total(
            internal, min_total, is_lab
        )
    return result


def get_grade(total):
    for grade, (min_mark, _) in GRADE_MAP.items():
        if total >= min_mark:
            return grade
    return "F"


def get_grade_point(grade):
    return GRADE_MAP.get(grade, (0, 0))[1]


def calculate_sgpa(subjects):
    total_points = 0
    total_credits = 0

    for sub in subjects:
        gp = sub.get("grade_point", 0)
        credits = float(sub.get("credits", 0))

        total_points += gp * credits
        total_credits += credits

    if total_credits == 0:
        return 0

    return round(total_points / total_credits, 2)


def check_honours_eligibility(sgpa):
    return sgpa >= 8.5


def calculate_sgpa_requirements(subjects_data, target_sgpa):
    """
    Calculate what external marks are needed per subject to achieve target SGPA.
    Returns a dict with each subject's requirements.
    """
    results = []
    total_credits = sum(sub["credits"] for sub in subjects_data)
    
    # Calculate total grade points needed to achieve target SGPA
    total_points_needed = target_sgpa * total_credits
    
    for sub in subjects_data:
        sub_credits = sub["credits"]
        internal = sub["internal"]
        is_lab = sub["is_lab"]
        
        # For this SGPA target, what grade would this subject need?
        best_grade_points = 10  # Maximum grade point is 10 for 'S'
        
        # Calculate minimum external needed to achieve best grade
        min_external_for_s = required_external_for_total(
            internal, 135, is_lab  # 'S' grade needs 135+ total
        )
        
        results.append({
            "code": sub["code"],
            "name": sub["name"],
            "credits": sub_credits,
            "external_for_s": min_external_for_s
        })
    
    return {
        "required_grade_points": total_points_needed,
        "total_credits": total_credits,
        "subjects": results
    }