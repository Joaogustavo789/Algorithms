def study_schedule(permanence_period, target_time):
    students_qt = 0

    if target_time is None:
        return None

    for student in permanence_period:
        if type(student[0]) is not int or type(student[1]) is not int:
            return None

        if target_time >= student[0] and target_time <= student[1]:
            students_qt = students_qt + 1

    return students_qt
