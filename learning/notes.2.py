#print(),input(),variables

name=input("what is your name")
print(name)
l=len(name)
print(l)
name="jenny"
print(name)
a=1
b="jio"
print(a)
print(b)

#swaping variables

a=input("enter the value of a=")
b=input("enter the VALUE OF B=")
c=a
a=b
b=c
print("a="+ a)
print("b="+ b)

#primitie data typs in python

print(0b10)
print(0o10)
print(0x10)
print(0b100)
print(0o1234567)
print(0x123456789)
var_1=3
var_2=30.00
var_3="charish"
var_4=True
var_5=False
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
print(type(var_5))
print(type(12345678907653799075211))
a=0b11011
print(type(a))
b=0e11011
print(type(b))
print(a)
print(b)
a=1
b=2
c=a>b
d=a<b
print(c)
print(d)
print(type(c))
print(type(d))

# "\"

print("jenny's \\n \n \"lecture's\"")

#operaters in python
#ex:- "+" , "-" , "*" , "/" , "//" , "**" , "%"

print(1234+5678)
print("charish " + "CHEEMAKURTHI")
print(5678-1234)
print(135*246)
print(10*"charish ")
print(98/98)
print(4//2)
print(9**2)
print(5%2)

a,b,c=2,4,6
print(a,c)
a += 3
print(a)
d=a+b
a+=5
d+=a
print(d)
a/=2
b*=2
c//=3
d**=0
print(a,b,c,d)

a,b=6,5
print(a<3 and b>7)
print(a>4 or b>9)
print(not(a))
print(not(a< 7))
print(not(b>7))
print(not(b))

a,b =5,4
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
print(a<<2)
print(a>>2)
print(b<<9)
print(b>>8)
print(a<<b)
print(a>>b)

a,b,c,d,e=5,5,5.0,6,"5"
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(a is b)
print(a is c)
print(a is d)
print(a is e)
print(b is c)
print(b is d)
print(b is e)
print(c is d)
print(c is e)
#print(d is e)
print(a == b)
print(a == c)
print(a == d)
print(a == e)
print(b == c)
print(b == d)
print(b == e)
print(c == d)
print(c == e)
print(d == e)

a="charish"
b=[2,3.0,67,-4,"charish"]
print( "c" in a)
print( 2 in b)
print( "cha" not in a)
print( 7 not in b)

#ROUND() FUNCTION

print(round(7))
print(round(7,2))
print(round(7.61))
print(round(2.6666,2))
print(round(2.6657,0))
print(round(7.22))

#f-strings :-

name="krishna"
age = 30
height=1.6
print(f"my name is {name}. I am {age} years old. my height is {height} meters")
print(f'{name}`s father  {age+28} years old')

#if else

age=int(input("enter your age"))
if age>18:
    print("eligible for voting")
else:
    print("not eligible for voting")

#elif

height=float(input("what is your height?"))
if height>=4.5:
    print("can ride")
    age=int(input("enter your age"))
    if age<=12:
        print("please pay 150 rs." )
    elif age<=18:
        print("please pay 250 rs.")
    else:
        print("please pay 500 rs.")
else:
    print("please pay 1000 rs.")
print("Thank You")

#lists

a =[1,2,3,4,5,1.3,4.89,"charish", True]
print(a)
b=[1,0,10,-4,-62,19]
print( b)
print(b[1])
print(b[:])
print(b[1:])
print(b [: 5])
print( b[2: 5])
print(b[3:3])
print(b [1 :6 :1])
print( b[0: 4 :2])
b .reverse()
print(b )
b.sort()
print( b)
b .reverse()
print(b )
print(min(b))
print(max(b))

#nested list

list1=[1,112,23,45,-90,[],[1,2.3,"abc",False]]
print(len(list1))
print(list1[5])
print(list1[6])
print(list1[6][0])
print(list1[6][1])
print(list1[6][2])
print(list1[6][3])
print(list1[6][len(list1[6])-1])
print(list1[6][::])
print(list1[6][0:])
print(list1[6][:4])
print(list1[6][0:4:2])

#seed function

import random as rd

rd.seed("charish")
print(rd.random())
print(rd.random())

import random as kd

print(kd.random())
print(kd.random())

#all functions in random module

print(dir(rd))
print()

#all functions in secrets module

import secrets
print(dir(secrets))

#getstate , set state

import random as r

a=r.getstate()
print(r.random())
print(r.randint(1,8))
print(r.uniform(0,6))

print()

r.setstate(a)
print(r.random())
print(r.randint(1,8))
print(r.uniform(0,6))

#randbytes

import random as c
print(c.randbytes(2))

#randrange

import random
print(random.randrange(1,2))
print(random.randrange(1,5,2))

#randint

import random
print(random.randint(1,2))
print(random.randint(1,5))
print(random.randint(5,10))
print(random.randint(0,9))

#choice , choices

from random import choices, choice
a=[1,2,3.4,5.6,'charish',True]
print(choices(a,[10,0,0,300,1,30],k=500))
print()
c=choice(a)
print(c)

#shuffle

import random as rm
a=[1,2,3,4,5]
rm.shuffle(a)
print(a)

#sample

from random import sample
a=[1,2.3,'abc',4,True]
print(sample(a,counts=[1,2,3,1,3],k=10))
print(sample(a,k=1))
print(sample(a,k=2))
print(sample(a,k=3))
print(sample(a,k=4))
print(sample(a,k=5))
print(sample(a,k=10,counts=[5,5,5,5,5]))

#binomialvarient

import random
#random.seed(2)
a=random.binomialvariate(0,0.5)
print(a)

#random

import random
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

#uniform

import random
print(random.uniform(1,10))
print(random.uniform(10,20))
print(random.uniform(20,30))
print(random.uniform(30,40))
print(random.uniform(40,50))

#tuples

tuple1=(1,2.3,"abc",True,True,2.3,1)
print(tuple1)
print(tuple1[1])
print(tuple1[-1])
print(type(tuple1))
tuple2=(45)
tuple3=(45,)
print(type(tuple2))
print(type(tuple3))
#tuple1[0]=12
#print(tuple1)
print(tuple1[:])
print(tuple1[2:])
print(tuple1[:5])
print(tuple1[2:4])
print(tuple1[::2])
a=tuple1[1:5:3]
print(list(a))
import random as r
print(r.choice(a))
print(len(tuple1))
print(tuple1,tuple2)
print(tuple1,tuple3)
tuple4=(tuple1,tuple3)
print(tuple4)
print(len(tuple4) , tuple1+tuple3 , tuple4[0] , tuple4[1])
tuple5=[1,2,9,0,6,8,45]
print(max(tuple5))
#print(max(tuple1))
list1=[12,34,98,76]
b=tuple(list1)
print(b)
c=list(b)
print(c)
print(tuple1.count("abc"))
print(tuple1.index(1))
d=(tuple1)*5
print(d)

#sets

set1={1,2,4.5,"abc",True,False,0}
set2={}
a=set()
print(set1)
print(type(set1))
print(type(set2))
print(type(a))
print(len(set1))
set1.add(3)
print(set1)
set1.remove(1)
print(set1)
set1.remove(0)
print(set1)
set1.discard(9)
print(set1)
#set1.remove(9)
#print(set1)
#set1.clear()
#print(set1)
print(set1.pop())
print(set1)
#we can add any tuple inside a set but we cant add a list to a set
#because set and tuple are immutable and liat is mutable
set1.add((1,2,3))
print(set1)
#set1.add([1,2,3])

#sets_2

set_1={"charish","anabelle","the nun","conjuring"}
set_2={"charish","triveni","janardhan rao","likhitha"}
set_3={"triveni","lavanya","kusuma kumari","subbarao"}
print(set_1.union(set_2))
print(set_1.union(set_2,set_3))
print(set_1 | set_2)
print(set_1 | set_2 |set_3)
print(set_1.union(["snow anna" , "snow uncle"]))
#print(set_1 | ["snow anna" , "snow uncle"])
set_1.update(set_3)
print(set_1)
set_2|=set_3
print(set_2)
set_1={"charish","anabelle","the nun","conjuring"}
set_2={"charish","triveni","janardhan rao","likhitha"}
set_3={"triveni","lavanya","kusuma kumari","subbarao"}
print(set_1.intersection(set_2))
print(set_1.intersection(set_2,set_3))
print(set_1 & set_2)
print(set_1 & set_2 & set_3 )
print(set_1.intersection(["snow anna" , "snow uncle"]))
# print(set_1 & ["snow anna" , "snow uncle"])
set_1.intersection_update(set_2)
print(set_1)
set_2.intersection_update(set_3)
print(set_2)

#sets_3

set_1={"charish","anabelle","the nun","conjuring"}
set_2={"charish","triveni","janardhan rao","likhitha"}
set_3={"triveni","lavanya","kusuma kumari","subbarao"}
print(set_1.difference(set_2))
print(set_2.difference(set_1 ,set_3))
print(set_1.difference(["snow anna" , "snow uncle"]))
print(set_1 - set_2)
print(set_2-set_1-set_3)
# print(set_1 - ["snow anna" , "snow uncle"])
set_1.difference_update(set_2)
print(set_1)
print(set_2)
set_1={"charish","anabelle","the nun","conjuring"}
print(set_1.symmetric_difference(set_2))
print(set_1.symmetric_difference(["snow anna" , "snow uncle"]))
# print(set_1.symmetric_difference(set_2,set_3))
print(set_1^set_2^set_3)
# print(set_1^["snow anna" , "snow uncle"])
set_1.symmetric_difference_update(set_2)
set_2.symmetric_difference_update(["snow anna" , "snow uncle"])
print(set_1)
print(set_2)

#sets_4

set_1={1,2,3,4,5,6,7,8,9,10}
set_2={3,4,5,6,7}
set_3={11,12,13,14,15}
print(set_2.isdisjoint(set_3))
print(set_1.isdisjoint(set_2))
print(set_2.isdisjoint(set_1))
print(set_1.issubset(set_2))
print(set_2.issubset(set_1))
print(set_1 <= set_2)
print(set_1.issuperset(set_2))
print(set_2.issuperset(set_1))
print(set_1 >= set_2)

#for loop

names=("charish","odfinrtgji","hgethth")
a=list(names)
b=tuple(a)
c=set(b)
# print(a)
# print(b)
for name_l in a:
    print(name_l)
print()
for name_t in b:
    print(name_t)
print()
for name_s in c:
    print(name_s)
print()
# print(list(name_))
d=[]
numbers=(1,-2,3.4,567)
for number in numbers:
    print(number)
for number in numbers:
    d.append(number)
    print(d)
    print()
print(d)
e="cheemakurthi charish"
for i in e:
    print(i)

# for else

a=[1,2,3,4,5,6,7,8,9,10]
for num in a:
    print(num)
else:
    print("code succesfully runed")

a=[1,2,3,4,5,6,7,8,9,10]
for num in a:
    if num%6==0 :
        print(num)
        break
    else:
        print("break not successful ")
else:
    print("code successfully runed")

# while loop

count=1
while count<=5:
    print(count)
    count+=1
print()
count=5
while count>-1: print(count);count-=1
else:print("in else block")
print("out from loop")
print()
count=1
while count<=5:
    print(count)
    count+=1
    if count==4:
        break
else:print("in else block")
print()
num=int(input("enter a number (enter 0 to quit)"))
tot=0
while num!=0:
    tot+=num
    num = int(input("enter a number (enter 0 to quit)"))
print(tot)

# break

a=["hi","hello","namasthe"]
b=["charish","cherry","chechu"]
for i in a:
    for k in b:
        print(i,k)
        if i=="namasthe" and k=="chechu":
            break
        print("hi")
    print("hi")
print("hi")
print()

# continue

a=["hi","hello","namasthe"]
b=["charish","cherry","chechu"]
for i in a:
    for k in b:
        print(i,k)
        if i=="namasthe" and k=="chechu":
            continue
        print("hi")
    print("hi")
print("hi")
print()

# pass

a=["hi","hello","namasthe"]
b=["charish","cherry","chechu"]
for i in a:
    for k in b:
        print(i,k)
        if i=="namasthe" and k=="chechu":
            pass
        print("hi")
    print("hi")
print("hi")

phone_no={"ram":1234,"shyam":5678,"mohan":9012}
phone_no1=dict([("ram",1234),("shyam",5678),("mohan",9012)])
print(phone_no)
print(phone_no1)
phone_no1["ram"]=789456
print(phone_no1)
phone_no["ram"]={"ram_home":201975 ,"ram_work":357890}
print(phone_no)
phone_no["shyam"]={623578,487,243856}
print(phone_no)
phone_no["ghef"]={2934}
print(phone_no)
del phone_no["ghef"]
print(phone_no)
phone_no.pop("shyam")
print(phone_no)
print(phone_no.values())
