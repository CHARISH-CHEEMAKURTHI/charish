name_1=input("enter your name").lower()
name_2=input("enter your loved one`s name").lower()
t=name_1.count("t")+name_2.count("t")
r=name_1.count("r")+name_2.count("r")
u=name_1.count("u")+name_2.count("u")
e=name_1.count("e")+name_2.count("e")
l=name_1.count("l")+name_2.count("l")
o=name_1.count("o")+name_2.count("o")
v=name_1.count("v")+name_2.count("v")
count_1=t+r+u+e
count_2=l+o+v+e
count=str(count_1)+str(count_2)+"%"
print(f"your love score is {count}")
score_1=str(count_1)+str(count_2)
score=int(score_1)
if score<10 :
    print("you both will blast every time like cocacola and mentos")
elif score>90 :
    print("you are made for each other")
elif 50<score<=90 :
    print("you both attract every time like magnets")
else:
    print("you can manage your love ")

