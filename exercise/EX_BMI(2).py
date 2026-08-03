Wt=int(input("enter your weight"))
H=float(input("enter your height"))
BMI=float(Wt/H**2)
print(BMI)
if BMI<16.0:
    print("under weight(severe thinness)")
if 16.0<=BMI<16.9:
        print("underweight(moderate thinness)")
if 17.0<=BMI<18.4:
        print("underweight(mild thinness)")
if 18.5<=BMI<24.9:
        print("normal range")
if 25.0<=BMI<29.9:
        print("overweight(pre-obese)")
if 30.0<=BMI<34.9:
        print("obese(class 1")
if 35.0<=BMI<39.9:
        print("obese(class 2)")
if BMI>=40.0:
        print("obese(class 3)")
print("THANK YOU")