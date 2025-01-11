from school import students, courses, grades


def main():   
    student = {}
    students_data = []
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]

    grades_data = []

    while True:
        print("\n=== Welcome to On-School ===","1. Register","2. Login","3. Exit", sep="\n")
        choise = int(input("Select an option: "))
        try: 
            choise != 1 or 2 or 3
        except ValueError:
            print("Iltimos mavjudbolgan option kiriting !")


        if choise == 1:
            new_student = students.register_student(student, students_data)
            students_data.append(new_student)

            print(f"Registration successful! Welcome, {(new_student["name"])}", end="\n")
        elif choise == 2:
            
            user = students.login_student(students_data)
            while user:
                
                print("\n--- Main Menu for Alice Smith --- \n")
                print("1. View Available Courses")
                print("2. Enroll in a Course")
                print("3. View My Courses")
                print("4. Check My Grades")
                print("5. Logout")
                print("6. exit")
                user_choose = int(input("Choose an option: "))

                if user_choose == 1:
                    courses.view_courses(courses_data)
                elif user_choose == 2:
                    user['course'].append(students.enroll_in_course(courses_data, students_data, user['password_login']['login']))
                elif user_choose == 3:
                    courses.view_courses(user['course'])  
                elif user_choose == 4:
                    grades.check_grades(user, grades_data)
                elif user_choose == 5:
                    break  
                elif user_choose == 6:
                    exit()
                else:
                    print(f"\n{user_choose} Option not find!\n")
                  
        elif choise == 3:
        
            print("exiting...")
            exit()

if __name__ == "__main__":
    main()