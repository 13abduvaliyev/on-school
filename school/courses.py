def view_courses(courses_data: list[dict[str, str]]) -> None:
    """
    Displays a list of available courses with details such as course name, duration, 
    and instructor.

    Args:
        courses_data (list): A list of dictionaries containing course details. 
                              Each dictionary has keys like 'course_name', 'instructor', and 'duration'.
    """
    
    
    print("\nAvailable Courses:")
    for kurs in range(len(courses_data)):
        print("{}. {} (Duration: {}, Instructor: {})".format(kurs + 1,courses_data[kurs]['course_name'], courses_data[kurs]["duration"], courses_data[kurs]["instructor"]))
