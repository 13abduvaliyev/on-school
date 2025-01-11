def check_grades(
        student_courses: dict, 
        grades_data: list 
        ) -> None:

    if len(grades_data) == 0:
        print("Grades:")
        for course in range(len(student_courses['course'])):
            print(f"{student_courses['course'][course]['course_name']}: Not graded yet")
