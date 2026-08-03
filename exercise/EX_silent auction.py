import os
bidders = {}
def winner():
    max_bid = max(bidders.values())
    for key, value in bidders.items():
        if max_bid == value:
            print(f"{key} wins!")
a=True
while a:
    name=input("enter your name:")
    bid=int(input("enter your bid:"))
    bidders[name] = bid
    conformation = input("are there any other bidders? yes/no:")
    if conformation =="no":
        a=False
        os.system("cls")
        winner()
    elif conformation =="yes":
        os.system("cls")
