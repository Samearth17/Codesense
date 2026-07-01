def get_grade_counts(student_info):
    scores_by_grade = {
        "As": 0,
        "Bs": 0,
        "Cs": 0,
        "Ds": 0
    }

    for student in student_info:
        for score in student["scores"]:
            if score >= 90:
                scores_by_grade["As"] += 1
            elif score >= 80:
                scores_by_grade["Bs"] += 1
            elif score >= 70:
                scores_by_grade["Cs"] += 1
            else:
                scores_by_grade["Ds"] += 1

    return scores_by_grade