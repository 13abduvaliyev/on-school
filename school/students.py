from pprint import pprint

def register_student(students_data: dict[str, dict[str, str]]) -> None:
    """
    Registers a new student by collecting their name, email, and password, 
    and stores the information in the students_data dictionary.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.
    """
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = {
        "name": name,
        "email": email,
        "password": password,
    }
    # TODO: 1. validate name, email 2. shifrlash password
    
    n = len(students_data)
    students_data[100000 + n + 1] = user

    print(f"Registration successful! Welcome, {name}.")

    return students_data

def login_student(students_data: dict[str, dict[str, str]]) -> int:
    """
    Allows a student to log in by entering their email and password. 
    If the login is successful, it returns the student's name.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.

    Returns:
        str: The student's name if login is successful, else None.
    """
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user_id in students_data:
        if students_data[user_id]['email'] == email and students_data[user_id]['password'] == password:
            print(f"Login successful! Welcome back, {students_data[user_id]['name']}.")
            return user_id

    print("User doesn't exist.")
    return -1

def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:
    """
    Allows a student to enroll in a course by selecting from the available courses. 
    The selected course is added to the student's list of enrolled courses.

    Args:
        courses_data (list): A list of dictionaries containing available course details.
        students_data (dict): A dictionary where student emails are keys 
                               and their details (including enrolled courses) are stored as values.
        student_email (str): The email of the student who is enrolling.
    """
    courses_number = int(input("Select a course number to enroll: "))

    if courses_number - 1 > len(courses_data) or courses_number - 1 < 0:
        print("\nBu raqamda kurs mavjud emas!, Iltimos boshqa raqam kiriting!\n")
        return None
    else:
        print("Successfully enrolled in {}!\n".format(courses_data[courses_number - 1]["course_name"]))
        return courses_data[courses_number - 1]
