def add_student(students):
    
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found!")
        return

    for student in students:
        print(student)


def search_student(students):
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found!")
            print(student)
            return

    print("Student not found!")
