#EXERCISE 1

a=input("enter a 2 digit no")
b=int(a[0])
c=int(a[1])
print(b +c)

#EXERCISE 2

weight=input("enter your weight in kg`s")
height=input("enter your height in meters")
Wt=int(weight)
H=float(height)**2
BMI=Wt/H
print(int(BMI))
#EXERCISE 3

age=int(input("enter your age"))
a=90-age
b=a*365
c=a*52
d=a*12
print(f"you have {b} days ,{c}weeks and {d} months left")

#EXERCISE 4

num=int(input("enter a number"))
n=num%2
if n==0:
    print("entered number is even number")
else:
    print("entered number is odd number")

#BITWISR OPERATOR

print(26 & 23)
print(17 | 24)
print(17 ^ 24)
print(~45)
print(68<<2)
print(56>>3)

#IDENTITI OPERATOR

a=5
print(id(a))
a=8
print(id(a))
print(a is a)