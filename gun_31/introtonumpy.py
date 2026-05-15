# numpy'ı np olarak kısaltıyoruz
import numpy as np

# numpy array
my_list = [10, 20, 30, 40]
my_numpy_array = np.array(my_list)
print(my_numpy_array)
print(type(my_numpy_array)) # <class 'numpy.ndarray'>

# index mantığı burada da aynıdır
print(my_numpy_array[-1])
my_numpy_array[0] = 100
print(my_numpy_array)

# maksimum, minimum, ortalama
print(my_numpy_array.max())
print(my_numpy_array.min())
print(my_numpy_array.mean())

# python lists kullanarak matris yazalım
matrix_list = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
# np.array ile numpy'a veriyoruz
np_matrix_list = np.array(matrix_list)
print(np_matrix_list)

# shape
print(np_matrix_list.shape) # (4, 3)

# arange
# klasik range'i, numpy array'i olarak oluşturur
print(list(range(0, 10))) # klasik range
print(np.arange(0, 10))
print(np.arange(0, 30, 2)) # 2'şer atlayarak gitme

# zeros
print(np.zeros(10)) # 10 tane 0 oluşturur
print(np.zeros((10, 10))) # 10 x 10 matrisi 0 ile doldurur, burada (10 , 10) tuple'ı shape'tir

# ones
print(np.ones((10, 10))) # 10 x 10 matrisi 1 ile doldurur

# linspace
print(np.linspace(0, 10, 5)) # 0'dan 10'a kadar eşit aralıklarla 5 elemanlı array oluşturur

# random
print(np.random.randint(0, 10)) # 0-10 arası rastgele sayı üretir
print(np.random.randint(0, 10, 3)) # elemanları 0-10 arası olan 3 elemanlı rastgele array oluşturur