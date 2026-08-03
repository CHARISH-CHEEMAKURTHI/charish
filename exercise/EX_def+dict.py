students_data = [
    {"name":"ram",
     "roll_no":10,
     "age":20,
     "course":"python",},
    {"name":"mohan",
     "roll_no":20,
     "age":22,
     "course":"java",},
]
def student_info(name, roll_no, age, course):
    student_data={
        "name":name,
        "roll_no":roll_no,
        "age":age,
        "course":course }
    students_data.append(student_data)
student_info("shyam",22,18,"c++")
print(students_data)