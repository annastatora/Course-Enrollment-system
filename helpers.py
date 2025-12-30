def check_non_empty_text(text):
    if text is None:
        return False

    cleaned = text.strip()
    if not cleaned:
        return False

    return True

def validate_age(age):
    if age is None:
        return False

    if not isinstance(age,int):
        return False

    if age < 5 or age > 120:
        return False

    return True

def validate_grade(grade):
    if grade is None:
        return False

    if not isinstance(grade,(int, float)):
        return False

    if grade < 2 or grade > 6:
        return False

    return True

def validate_course_code(code):
    if code is None:
        return False

    cleaned = code.strip()
    if not cleaned:
        return False

    return True


