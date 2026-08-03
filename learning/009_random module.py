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