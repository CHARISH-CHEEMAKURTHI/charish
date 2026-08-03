import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([[1,2,3,4,5],[6,7,8,9,0]])

print(a)
print(b)
print(b[1,3])
print(b[:,0])
print(b[0,:])
print(b[:])
print(b[0,0:3:2])
print(b[1:4:2,0])
a[1]=3
print(a)
b[:,2]=[1,2]
b[:,3]=[7]
print(b)
b[0,:]=[5]
print(b)
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c[0,1,0])
c[0,1,0]=8
print(c)

print(a.shape)

print(np.__version__)