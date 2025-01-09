from os import system

from school.students import register_student, enroll_in_course, login_student, logout
from school.courses import view_courses
from school.grades import check_grades

def show_menu(
        menu: list[tuple[int, str]],
        user: dict = {}
    ) -> None:

    print(
        "=== Welcome to On-School ===" if len(menu) == 3 else f"\n--- Main Menu for {user['name']} ---",
        end="\n\n"
    )
    
    for option in menu:
        print(f'{option[0]}. {option[1]}', end="\n")

def main() -> None:
    """
    Main function that drives the On-School system. It displays the main menu, 
    handles user registration and login, and provides an interface for enrolled students 
    to interact with courses and check grades.
    """
    students_data = {
        100001: {
            'email': 'example@gmail.com',
            'name': 'Ali Valiyev',
            'password': '1234'
        },
        100002: {
            'email': 'bjfkabdsfabds',
            'name': 'jkfbadjsbf',
            'password': '324512345'
        }
    }
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]
    grades_data = {}

    menu = [
        (1, "Register"), (2, "Login"), (3, "Exit")
    ]

    user_menu = [
        (1, "View Available Courses"),
        (2, "Enroll in a Course"),
        (3, "View My Courses"),
        (4, "Check My Grades"),
        (5, "Logout")
    ]

    system('clear')

    while True:
        while not user:
            show_menu(menu, user)
            choice = input("\nSelect an option: ")

            if choice == "1":
                students_data = user.register_student(students_data)
            elif choice == "2":
                user_id = user.login_student(students_data)
            elif user_id == '3':
                print("\nExiting ...")
                exit()

        while user:
            show_menu(user_menu, user=students_data[user_id])
            
            user_choice = input("Choose an option: ")
            
            if user_choice == '1':
                view_courses(courses_data)
            elif user_choice == '2':
                user['cource'].append(enroll_in_course(courses_data, user))
            elif choice == "3":
                view_courses(user["courses"])
            elif choice == "4":
                check_grades(grades_data, user["email"])
            elif choice == "5":
                user = logout()


if __name__ == "__main__":
    main()
