import numpy as np

a=np.zeros([4,3,2,2,2])
print(a)
b=np.ones([2,3,4,5])
print(b)
c=np.full([2,3],79)
print(c)
d=np.random.rand(3,5)
print(d)
e=np.random.random_sample(a.shape)
print(e)
f=np.random.randint(10,size=(3,3))
print(f)
g=np.identity(4)
print(g)
h=np.array([9,8])
i=np.repeat(h,5)
print(i)
j=h
k=h.copy()
j[0]=1
k[1]=2
print(j)
print(h)
print(k)