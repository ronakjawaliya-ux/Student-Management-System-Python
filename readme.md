# 🎓 Student Management System (Python)

A simple **Student Management System** built using **Python** that allows users to manage student records through a command-line interface (CLI). Student data is stored permanently using **JSON**, ensuring records remain available even after the program is closed.

---

## 📌 Features

* ✅ Add New Student
* ✅ View All Students
* ✅ Search Student by ID
* ✅ Update Student Details
* ✅ Delete Student Record
* ✅ Display Total Number of Students
* ✅ Clear All Student Records
* ✅ Automatic Data Saving using JSON
* ✅ Input Validation and Error Handling

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)

---

## 📂 Project Structure

```text
Student-Management-System-Python/
│
├── main.py              # Main application
├── students.json        # Stores student records
└── README.md            # Project documentation
```

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/ronakjawaliya-ux/Student-Management-System-Python.git
```

2. Open the project folder.

3. Run the program:

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Total Students
7. Clear Students
8. Exit
```

---

## 💡 Features Explained

### ➕ Add Student

* Adds a new student record.
* Stores student details in `students.json`.

### 📋 View Students

* Displays all student records in the system.

### 🔍 Search Student

* Searches for a student using the Student ID.
* Displays student information if found.

### ✏️ Update Student

* Updates an existing student's details.
* Saves changes automatically.

### 🗑️ Delete Student

* Deletes a student record using the Student ID.

### 👥 Total Students

* Displays the total number of students currently stored.

### 🧹 Clear Students

* Removes all student records after confirmation.

---

## ⚠️ Input Validation

The application handles several invalid inputs, including:

* Invalid Student IDs
* Duplicate Student IDs (if implemented)
* Student not found
* Empty student records
* Invalid user input
* Automatic handling of missing or corrupted JSON files

---

## 📷 Sample Output

```text
===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Total Students
7. Clear Students
8. Exit

Enter your choice: 2

Student ID : 101
Name       : Ronak
Age        : 22
Course     : B.Tech CSE (AI & ML)
```

---

## 🎯 Future Improvements

* 📊 Display students sorted by name or ID
* 📈 Grade and percentage management
* 📄 Export student records to CSV
* 🔐 Login authentication
* 🗄️ SQLite/MySQL database integration
* 🖥️ GUI using Tkinter
* 🌐 Web version using Flask or Django

---

## 📚 What I Learned

This project helped me practice:

* Python Fundamentals
* Functions
* Loops and Conditional Statements
* Lists and Dictionaries
* CRUD Operations
* JSON File Handling
* Exception Handling
* Problem Solving
* Building a Complete CLI Application

---

## 👨‍💻 Author

**Ronak Jawalia**

* B.Tech CSE (AI & ML)
* Python Developer
* Learning Data Structures & Algorithms
* Building projects to strengthen programming skills

### GitHub

* **Profile:** https://github.com/ronakjawaliya-ux
* **Repository:** https://github.com/ronakjawaliya-ux/Student-Management-System-Python

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to keep learning and building more projects!
