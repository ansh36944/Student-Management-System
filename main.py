import json

from student import add_student, view_students, search_student


# Load student data into json file
try:
    with open("students.json", "r") as file:
        students = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    students = []


# Main application
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        add_student(students)

        # Save data automatically
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Data saved successfully!")
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")
