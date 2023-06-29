#School administration program
import csv

def write_to_csv(student_info):
    with open('student_records.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_info)

def read_from_csv():
    with open('student_records.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def take_student_info():
    name = input("Enter student name: ")
    roll_number = input("Enter student roll number: ")
    phone_number = input("Enter student phone number: ")
    student_info = [name, roll_number, phone_number]
    return student_info

def main():
    while True:
        print("\nSchool Administration Program")
        print("1. Add Student Records")
        print("2. View Student Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            student_info = take_student_info()
            write_to_csv(student_info)
            print("Student record added successfully!")
        elif choice == '2':
            print("\n--- Student Records ---")
            read_from_csv()
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == '__main__':
    main()
