# pandas'ı pd olarak kısaltıyoruz
import pandas as pd
import numpy as np

# series
my_dict = {"James": 50, "Lars": 60, "Kirk": 55, "Rob": 65}
print(pd.Series(my_dict)) # serie oluşturma
age_list = [50, 60, 55, 65]
name_list = ["James", "Lars", "Kirk", "Rob"]
print(pd.Series(age_list, name_list))
print(pd.Series(data=age_list, index=name_list)) # hangisinin data hangisinin index olduğunu belirtmek daha iyidir

# numpy array'den serie üretme
numpy_array = np.arange(0, 8)
print(pd.Series(numpy_array)) # indeksleri kendisi verecektir

# serie'lerde toplama
exam_results1 = pd.Series(data=[70, 60, 100], index=["A", "B", "C"])
exam_results2 = pd.Series(data=[80, 30, 50], index=["A", "D", "C"])
print(exam_results1 + exam_results2) # B ve D değerlerindeki toplamlar nan olur