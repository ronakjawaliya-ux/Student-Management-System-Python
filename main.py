#  Project-01 || Student Management System
#  Using Python

import json


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

students = load_students()


while True:
    print("\n===== Student Management System =====\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Clear Students")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # 1. ADD_STUDENTS
    if choice == "1":
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")

        student = {
                 "id": student_id,
                 "name": name,
                 "age": age,
                 "course": course
        }

        found = False

        for existing_student in students:
            if existing_student["id"] == student_id:
                 found = True
                 print("\nStudent ID Already Exists.")
                 break

        if not found:
            students.append(student)
            print("Student added successfully!")
            save_students()


    # 2. VIEW_STUDENTS
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in students:
                print("------------------------------------")
                print("ID:",student["id"])
                print("Name:",student["name"])
                print("Age:",student["age"])
                print("Course:",student["course"])


    # 3. SEARCH_STUDENTS
    elif choice == "3":
        search_id = int(input("Enter student ID to search: "))

        found = False

        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                found = True
                break

        if not found:
            print("Student not found.")


    # 4. UPDATE_STUDENTS
    elif choice == "4":
        update_id = int(input("Enter student ID to update: "))

        found = False

        for student in students:
            if student["id"] == update_id:
                student["name"] = input("Enter new name: ")
                student["age"] = input("Enter new age: ")
                student["course"] = input("Enter new course: ")
                print("Student updated successfully!")
                save_students()
                found = True
                break

        if not found:
            print("Student not found.")


    # 5. DELETE_STUDENTS
    elif choice == "5":
        delete_id = int(input("Enter student ID to delete: "))

        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("Student deleted successfully!")
                save_students()
                found = True
                break

        if not found:
            print("Student not found.")


    # 6. TOTAL_STUDENTS
    elif choice == "6":
        print("Total Students:",len(students))


    # 7. CLEAR_STUDENTS
    elif choice == "7":
        students.clear()
        print("All students are cleared successfully!")
        save_students()

    # 8. EXIT
    elif choice == "8":
        print("Thank you for using Student Management System!")
        break

    else:
        print("This option will be added later.")



