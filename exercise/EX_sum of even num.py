sum=0
for i in range(101):
    if i%2==0 :
        sum+=i
print(sum)
print()

# fizz buzz

for i in range(101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0 :
        print("buzz")
    else:
        print(i)