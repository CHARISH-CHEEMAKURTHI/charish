student_marks={"jenny":92,
               "harry":78,
               "dimpy":56,
               "rahul":41,
               "aniket":99,
               "prem":34}
for key, value in student_marks.items():
    if value <= 40:
        print(f"{key} got {value} marks and {key}`s grad is f")
    elif value <= 50:
        print(f"{key} got {value} marks and {key}`s grad is D")
    elif value <= 60:
        print(f"{key} got {value} marks and {key}`s grad is C")
    elif value <= 70:
        print(f"{key} got {value} marks and {key}`s grad is B")
    elif value <= 80:
        print(f"{key} got {value} marks and {key}`s grad is B+")
    elif value <= 90:
        print(f"{key} got {value} marks and {key}`s grad is A")
    elif value <= 100:
        print(f"{key} got {value} marks and {key}`s grad is A+")