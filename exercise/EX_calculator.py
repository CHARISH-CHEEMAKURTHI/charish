num_1=int(input("enter first number:"))
print("+ \n- \n* \n/ ")
ans=0
def new():
    global num_1
    global ans
    operation=input("pick an operation:")
    num_2=int(input("enter next number:"))
    if operation=="+":
        ans=num_1+num_2
        print(f"{num_1} {operation} {num_2} = {ans}")
        return ans
    elif operation=="-":
        ans= num_1 - num_2
        print(f"{num_1} {operation} {num_2} = {ans}")
        return ans
    elif operation=="*":
        ans= num_1*num_2
        print(f"{num_1} {operation} {num_2} = {ans}")
        return ans
    elif operation=="/":
        ans= num_1/num_2
        print(f"{num_1} {operation} {num_2} = {ans}")
        return ans
    else:
        print("invalid operation")
        ans=0
        return ans

def calculate():
    global num_1
    global ans
    ans=new()
    conformation=input(f"enter 'y' to continue calculation with {ans} or 'n' to start a new calculation or 'x' to exit:")
    if conformation=="y":
            num_1 = ans
            calculate()
    elif conformation=="n":
        num_1 = int(input("enter first number:"))
        print("+ \n - \n * \n / ")
        ans = 0
        calculate()
    elif conformation=="x":
        pass
    else:
        print("invalid input")
calculate()
