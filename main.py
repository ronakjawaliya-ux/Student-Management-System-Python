#  Project--01 | Student-Management-System
#  Using Python

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Clear Students")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # ADD_STUDENTS
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
        students.append(student)
        print("Student added successfully!")


    # VIEW_STUDENTS
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


    # SEARCH_STUDENTS
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


    # UPDATE_STUDENTS
    elif choice == "4":
        update_id = int(input("Enter student ID to update: "))

        found = False

        for student in students:
            if student["id"] == update_id:
                student["name"] = input("Enter new name: ")
                student["age"] = input("Enter new age: ")
                student["course"] = input("Enter new course: ")
                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")


    # DELETE_STUDENTS
    elif choice == "5":
        delete_id = int(input("Enter student ID to delete: "))

        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")


    # TOTAL_STUDENTS
    elif choice == "6":
        print("Total Students:",len(students))


    # CLEAR_STUDENTS
    elif choice == "7":
        students.clear()
        print("All students are cleared successfully!")


    # EXIT
    elif choice == "8":
        print("Thank you for using Student Management System!")
        break

    else:
        print("This option will be added later.")



