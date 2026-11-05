# Attendance Monitoring System with Teacher and Student roles

attendance = {}       # {date: {student: status}}
students = []         # list of student names
passwords = {}        # {student_name: password}
student_ids = {}      # {student_name: student_id}

TEACHER_PASSWORD = "teacher123"  # teacher's password


# ================= TEACHER FUNCTIONS =================

def teacher_menu():
    while True:
        print("\n===== TEACHER MENU =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Take Attendance")
        print("4. View Attendance (by date)")
        print("5. Back to Main Menu")

        choice = input("Choose (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            take_attendance()
        elif choice == "4":
            view_attendance_by_date()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return
    if name in students:
        print("⚠️ Student already exists.")
        return

    password = input(f"Set password for {name}: ").strip()
    
    # Student ID input with validation to ensure it is digits only
    student_id = input(f"Enter Student ID number for {name}: ").strip()
    if not student_id.isdigit():
        print("❌ Invalid Student ID. It must contain numbers only.")
        return

    students.append(name)
    passwords[name] = password
    student_ids[name] = student_id
    print(f"✅ {name} added with ID {student_id}.")


def view_all_students():
    if not students:
        print("📭 No students yet.")
        return
    print("\n--- Students ---")
    for i, s in enumerate(students, 1):
        s_id = student_ids.get(s, "N/A")
        print(f"{i}. {s} (ID: {s_id})")


def take_attendance():
    if not students:
        print("❌ No students to take attendance for.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not date:
        print("❌ Date required.")
        return

    attendance[date] = {}
    print(f"\nTaking attendance for {date}")
    for student in students:
        while True:
            status = input(f"Is {student} present? (p/a): ").strip().lower()
            if status == "p":
                attendance[date][student] = "Present"
                break
            elif status == "a":
                attendance[date][student] = "Absent"
                break
            else:
                print("❌ Enter 'p' or 'a' only.")

    print(f"✅ Attendance saved for {date}.")


def view_attendance_by_date():
    if not attendance:
        print("📭 No attendance records.")
        return
        
    date = input("Enter date to view: ").strip()
    if not date:
        print("❌ Date cannot be empty.")
        return
        
    if date not in attendance:
        print(f"❌ No record for {date}.")
        return

    # Check if attendance is complete (i.e., all registered students have a record for this date)
    if len(attendance[date]) != len(students):
        print("❌ Error: Attendance record is incomplete for this date.")
        return

    print(f"\n--- Attendance on {date} ---")
    for name, status in attendance[date].items():
        print(f"{name}: {status}")


# ================= STUDENT FUNCTIONS =================

def student_menu():
    name = input("Enter your name: ").strip()

    if name not in students:
        print("❌ Student not found.")
        return

    password = input("Enter your password: ").strip()
    if passwords.get(name) != password:
        print("❌ Wrong password.")
        return

    print(f"\n👋 Welcome, {name} (ID: {student_ids.get(name)})!")
    print("--- Your Attendance ---")

    found = False
    for date, records in attendance.items():
        if name in records:
            print(f"{date}: {records[name]}")
            found = True

    if not found:
        print("📭 No attendance record for you yet.")

    print("\n(You can only view — you cannot change your attendance.)")


# ================= MAIN MENU =================

def main():
    while True:
        print("\n===== ATTENDANCE MONITORING SYSTEM =====")
        print("1. Teacher Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Choose (1-3): ")

        if choice == "1":
            pwd = input("Enter teacher password: ").strip()
            if pwd == TEACHER_PASSWORD:
                print("✅ Teacher login successful.")
                teacher_menu()
            else:
                print("❌ Wrong password.")

        elif choice == "2":
            student_menu()

        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()