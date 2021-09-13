import numpy as np

# ndarray - arange, zeros, ones

print("\nndarray =================================================\n")
sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

one_arrya = np.ones((3, 2))
print(one_arrya)
print(one_arrya.dtype, one_arrya.shape)

#차원 크기 변경 reshape()

print("\n차원 크기 변경=================================================\n")
array1 = np.arange(10)
print('array1:\n', array1)
array2 = array1.reshape(2, 5)
print("array2:\n", array2)
array3 = array1.reshape(5, 2)
print("array3:\n", array3)
#array1.reshpae(4, 3)

array1 = np.arange(10)
print(array1)
array2 = array1.reshape(-1, 5)
print('array2 shape:', array2.shape)
array3 = array1.reshape(5, -1)
print("array3 shape:", array3.shape)

array1 = np.arange(8)
array3d = array1.reshape((2, 2, 2))
print("array3d:\n", array3d.tolist())

# 3차원 ndarray를 2차원으로 변환
array5 = array3d.reshape(-1, 1)
print("array5:\n", array5.tolist())
print("array5 shape:", array5.shape)

# 1차원 -> 2차원
array6 = array1.reshape(1, -1)
print("array6:\n", array6.tolist())
print("array6 shape:", array6.shape)

# 팬시 인덱싱
print("\n팬시 인덱싱=================================================\n")

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)

array3 = array2d[[0, 1],2]
print("array2d[[0, 1], 2] =>", array3.tolist())

array4 = array2d[[0,1], 0:2]
print("array2d[[0,1], 0:2] =>", array4.tolist())

array5 = array2d[[0,1]]
print("array2d[[0,1]] =>", array5.tolist())