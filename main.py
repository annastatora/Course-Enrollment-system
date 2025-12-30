from student import Student
import helpers

students = {}
courses = {}

def add_student(students):
    student_id = input("Enter student ID: ")
    if not helpers.check_non_empty_text(student_id):
        print("Invalid student ID.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter name: ")
    if not helpers.check_non_empty_text(name):
        print("Invalid name.")
        return

    age_text = input("Enter age: ")
    try:
        age_int = int(age_text)
    except ValueError:
        print("Age must be a number.")
        return

    if not helpers.validate_age(age_int):
        print("Invalid age.")
        return


    student = Student(student_id, name, age_int)
    students[student_id] = student
    print("Student added successfully.")


def show_all_students(students):
    if not students:
        print("No students. ")
        return

    for student in students.values():
        print(student)

def add_course(courses):
    course_code = input("Enter course code: ")
    if not helpers.validate_course_code(course_code):
        print("Invalid course code.")
        return

    course_code = course_code.strip().upper()

    if course_code in courses:
        print("Course already exists.")
        return

    course_name = input("Enter course name: ")
    if not helpers.check_non_empty_text(course_name):
        print("Invalid course name.")
        return

    courses[course_code] = course_name
    print("Course added successfully.")


def enroll_student(students,courses):
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    course_code = input("Enter course code: ")
    if not helpers.validate_course_code(course_code):
        print("Invalid course code.")
        return

    course_code = course_code.strip().upper()

    if course_code not in courses:
        print("Course not found.")
        return

    if student.enroll(course_code):
        print("Student enrolled successfully.")
    else:
        print("Student is already enrolled in this course.")


def add_grade_to_student(students):
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    course_code = input("Enter course code: ")
    if not helpers.validate_course_code(course_code):
        print("Invalid course code.")
        return

    course_code = course_code.strip().upper()

    grade_text = input("Enter grade (2–6): ")
    try:
        grade = float(grade_text)
    except ValueError:
        print("Grade must be a number.")
        return

    if not helpers.validate_grade(grade):
        print("Invalid grade.")
        return

    if student.add_grade(course_code, grade):
        print("Grade added successfully.")
    else:
        print("Student is not enrolled in this course.")


def mark_attendance(students):
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    course_code = input("Enter course code: ")
    if not helpers.validate_course_code(course_code):
        print("Invalid course code.")
        return

    course_code = course_code.strip().upper()

    if student.add_attendance(course_code):
        print("Attendance marked successfully.")
    else:
        print("Student is not enrolled in this course.")

def main_menu():
    while True:
        print("\n=== Student Enrollment System ===")
        print("1) Add student.")
        print("2) Show all students.")
        print("3) Add course.")
        print("4) Enroll student in course.")
        print("5) Add grade to student.")
        print("6) Mark attendance.")
        print("7) Exit.")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            add_course(courses)
        elif choice == "4":
            enroll_student(students, courses)
        elif choice == "5":
            add_grade_to_student(students)
        elif choice == "6":
            mark_attendance(students)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main_menu()
