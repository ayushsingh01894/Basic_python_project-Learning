# Student Management System

students = {}  # Dictionary to store student data

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
    else:
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))
        students[roll] = {"Name": name, "Course": course, "Marks": marks}
        print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found!")
    else:
        print("\n---- Student Records ----")
        for roll, data in students.items():
            print(f"Roll No: {roll}")
            print(f"Name: {data['Name']}")
            print(f"Course: {data['Course']}")
            print(f"Marks: {data['Marks']}\n")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        data = students[roll]
        print(f"\nRecord Found for Roll No {roll}:")
        print(f"Name: {data['Name']}")
        print(f"Course: {data['Course']}")
        print(f"Marks: {data['Marks']}")
    else:
        print("Student not found!")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        print("Enter new details:")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))
        students[roll] = {"Name": name, "Course": course, "Marks": marks}
        print("Record updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Record deleted successfully!")
    else:
        print("Student not found!")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter between 1-6.")

if __name__ == "__main__":
    main()
