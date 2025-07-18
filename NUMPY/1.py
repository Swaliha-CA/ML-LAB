import numpy as np
arr1=np.array((1,2,3,4))
print(arr1)
print()
arr1=arr1.reshape((2,2))
print(arr1)
print()

arr1=arr1.flatten()
print(arr1)
print()

arr2=np.array([[2,3],[5,6]])
print(arr2)
print()

arr3=np.array([10,20,30,40])
print(arr3)
print()

zeros=np.zeros((2,2))
print(zeros)
print()
ones=np.ones((2,3))
print(ones)
print()

result_add=arr1+5
print(result_add)
print()

result_mul=arr1*2
print(result_mul)
print()

result_elem_add=arr1+arr3
print(result_elem_add)
print()

result_elem_mul=arr1*arr3
print(result_elem_mul)
print()


sum_all=arr1.sum()
print(sum_all)
print()

mean_val=arr2.mean()
print(mean_val)
print()

max_val=arr2.max()
print(max_val)
print()


min_val=arr2.min()
print(min_val)
print()

sum_column=arr2.sum(axis=0)
print(sum_column)
print()

sum_row=arr2.sum(axis=1)
print(sum_row)
print()







