import random

print("enter, 0 for rock \n       1 for paper \n       2 for scissors")
print()
user_choice=int(input("enter your number as per instructions:"))
computer_choice=random.randint(0,2)
print(f"computer`s choice is {computer_choice}")
if computer_choice==0 and user_choice==0:
    print("rock Vs rock")
    print("draw")
elif computer_choice==0 and user_choice==1:
    print("rock Vs paper")
    print("user wins")
elif computer_choice==0 and user_choice==2:
    print("rock Vs scissors")
    print("computer wins")
elif computer_choice==1 and user_choice==0:
    print("paper Vs rock")
    print("computer wins")
elif computer_choice==1 and user_choice==1:
    print("paper Vs paper")
    print("draw ")
elif computer_choice==1 and user_choice==2:
    print("paper Vs scissors")
    print("user wins")
elif computer_choice==2 and user_choice ==0:
    print("scissors Vs rock")
    print("user wins")
elif computer_choice==2 and user_choice==1:
    print("scissors Vs paper")
    print("computer wins")
elif computer_choice==2 and user_choice==2:
    print("scissors Vs scissors")
    print(" draw")
else:
    print("you entered a wrong number")

