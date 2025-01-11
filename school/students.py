def register_student(student: dict[str, dict[str, str]], student_date: list) -> None:

    student_name = input("Enter your name: ")

    email = input("Enter your email: ")
    pasword = input("Enter your password: ")
    
    while True:
        length = len(pasword)
        
        if length < 8:
            print("Belgilar soni 8 dan kam bolmasligi kerak")
            pasword = input("Enter your password: ")      
        else:
            check_log_count = 0
            for user in range(len(student_date)):
                if student_date[user]['password_login']['login'] == email:
                    print("Bunaqa emailda foydalanuvchi ruyxatdan o`tgan, iltimos boshqa gmaildan foydalanib ko`ring")
                    email = input("Enter your email: ")
                    check_log_count +=1
                    break
            if check_log_count:
                pass
            else:
                break
    student = {
            'name': student_name, 
            'course': [], 
            'password_login': {'login': email, 
                        'password': pasword
                        }}
    return student

def login_student(students_data: list):
   
    login = input("Enter your email: ")
    password = input("Enter your password: ")

    student_dic = {}
    student_dic['login'] = login
    student_dic['password'] = password
    
    for user in students_data:
        if(user['password_login']) == student_dic:
            print(f"Login successful! Welcome back, {user['name']}.")
            return user
    return None

def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    email: str
) -> None:
 
    courses_number = int(input("Select a course number to enroll: "))

    if courses_number - 1 > len(courses_data) or courses_number - 1 < 0:
        print("Bunday kurs yuq")
        return None
    else:
        print("Successfully enrolled in {}!\n".format(courses_data[courses_number - 1]["course_name"]))
        return courses_data[courses_number - 1]
   