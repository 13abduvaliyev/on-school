def view_courses(courses_data: list):
    print("\nAvailable Courses:")
    for i in range(len(courses_data)):
        print(f"{i + 1}. {courses_data[i]['course_name']} (Duration: {courses_data[i]["duration"]}, Instructor: {courses_data[i]["instructor"]})")