import numpy as np
list1 = [10, 20, 30, 40, 50]
array_one=np.array(list1)
print(array_one,array_one.ndim,array_one.shape,array_one.size,array_one.dtype, array_one.itemsize, array_one.nbytes)
list2 =[[1, 2, 3], [4, 5, 6]]
array_two=np.array(list2)
print(array_two,array_two.ndim,array_two.shape,array_two.size,array_two.dtype, array_two.itemsize, array_two.nbytes)
martix=np.matrix(([[1, 2, 3], [4, 5, 6],[7, 8, 9]]))
print("Matrix",martix)