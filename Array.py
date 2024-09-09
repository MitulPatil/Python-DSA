from array import *

arr = array('i', [10,20,30,40])

print(type(arr))
print(arr)

#iteration using for loop
for i in arr:
    print(i)

for i in range(4):
    print(arr[i],end=' ')

#iteration using while loop
i=0
while(i<len(arr)):
    print(arr[i])
    i+=1

# array methods :

# append() :- append element at the end of the array

arr.append(50)
print(arr)

# count() :- It give the count how many times element present in array

print(arr.count(30))

# extend() :- append another array at the end of the another array

arr2= array('i',[90,80])

arr.extend(arr2)
print(arr)

# formlist() :- append list to the end of the array

l=[1,2,3,4]
arr.fromlist(l)
print(arr)

# index() :- give index of array element

print(arr.index(40))

# insert() :- insert element to the certain position

arr.insert(3,70)
print(arr)

# pop() :- delete element form end but you can specify index to delete 

arr.pop()
print(arr)
arr.pop(3)
print(arr)

# remove() :- to delete array element 

arr.remove(50)
print(arr)

# reverse() :- reverse the array

arr.reverse()
print(arr)

# tolist() :- convert array to list  

list=arr.tolist()
print(list)

# Array using Numpy package

import numpy as np

a1 = np.array([1,2,3]) # 1D array
print(a1)

a2 = np.array([[1,2,3],[4,5,6]]) # 2D array
print(a2)
