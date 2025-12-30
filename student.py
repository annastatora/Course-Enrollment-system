class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.enrollment = {}

    def enroll(self, course_code):
        if course_code is None:
            print("Invalid.")
            return False

        cleaned = course_code.strip()
        if not cleaned:
            return False
        cleaned = cleaned.upper()

        if cleaned in self.enrollment:
            return False

        self.enrollment[cleaned] = {
            "grades": [],
            "attendance": 0
        }
        return True

    def add_grade(self,course_code,grade):
        if course_code is None:
            return False
        cleaned_code = course_code.strip()
        if not cleaned_code:
            return False

        cleaned_code = cleaned_code.upper()

        if cleaned_code not in self.enrollment:
            return False

        if not isinstance(grade,(int,float)):
            return False

        if grade < 2 or grade > 6:
            return False

        self.enrollment[cleaned_code]["grades"].append(grade)
        return True

    def add_attendance(self,course_code):
        if course_code is None:
            return False
        cleaned_code = course_code.strip()
        if not cleaned_code:
            return False

        cleaned_code = cleaned_code.upper()

        if cleaned_code not in self.enrollment:
            return False

        self.enrollment[cleaned_code]["attendance"] += 1
        return True

    def __str__(self):
        result = (
            f"Student ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Enrolled courses: {len(self.enrollment)}"
        )

        for course, data in self.enrollment.items():
            result += (
                f"\n  Course: {course}, "
                f"Grades: {data['grades']}, "
                f"Attendance: {data['attendance']}"
            )

        return result









