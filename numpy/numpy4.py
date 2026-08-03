import numpy as np

a=np.array([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20]])
print(np.sum(a,axis=0))
print(np.sum(a))
print(np.mean(a))
print(np.std(a))
print(np.max(a))
print(np.min(a))
print(np.median(a))
print(np.percentile(a,50))
print(np.percentile(a,75))
print(np.percentile(a,25))
print(np.argmin(a))
print(np.argmax(a))
print(np.var(a))

