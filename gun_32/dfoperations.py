import numpy as np
import pandas as pd

# eksik veriler
my_dict = {"James" : [40, 30, np.nan], "Kirk" : [20, np.nan, 50], "Lars" : [30, 50, 40]}
my_df = pd.DataFrame(my_dict)
print(my_df)
print(my_df.dropna()) # eksik veri bulunan satırları siler
print(my_df.dropna(axis=1)) # eksik veri bulunan sütunları siler

my_new_dict = {"James" : [40, 30, np.nan], "Kirk" : [20, np.nan, 50], "Lars" : [30, 50, 40], "Rob": [45, np.nan, np.nan]}
my_new_df = pd.DataFrame(my_new_dict)
print(my_new_df)
print(my_new_df.dropna(axis=1, thresh=2)) # bir sütun kalacaksa en az 2 dolu değer taşımalı
print(my_new_df.fillna(20)) # boş değerleri 20 ile doldur

# groupy
salary_dict = {"Programming Languages": ["Python", "Python", "Python", "Java", "Java", "R"],
               "Name": ["Ali", "Bekir", "Cevdet", "Derya", "Erdal", "Faruk"],
               "Salary": [100, 90, 80, 70, 60, 50]}
salary_df = pd.DataFrame(salary_dict)
print(salary_df)
group_object = salary_df.groupby("Programming Languages") # yazılım dillerine göre gruplara ayır
print(group_object.count()) # her grubun (yazılım dili) sütunlardaki sayıları
print(group_object.mean(numeric_only=True)) # her grubun ortalamaları
print(group_object.min(numeric_only=True)) # minimum
print(group_object.max(numeric_only=True)) # maksimum

print(group_object.describe()) # genel özet tablosu verir

# df birleştirme
my_dict1 = {"Name" : ["A","B","C","D"],
           "Sports" : ["Basketball", "Football", "Tennis", "Running"],
            "Calories" : [100,200,300,400]
           }
my_df1 = pd.DataFrame(my_dict1, index=[0,1,2,3])

my_dict2 = {"Name" : ["E","F","G","H"],
           "Sports" : ["Basketball", "Football", "Tennis", "Running"],
            "Calories" : [200,50,330,440]
           }
my_df2 = pd.DataFrame(my_dict2, index=[4,5,6,7]) # indeksleri biz vermezsek birleştiğinde sıralı olmaz

my_dict3 = {"Name" : ["I","J","K","L"],
           "Sports" : ["Basketball", "Football", "Tennis", "Running"],
            "Calories" : [300,150,320,410]
           }
my_df3 = pd.DataFrame(my_dict3, index=[8,9,10,11])

# concenation
print(pd.concat([my_df1, my_df2, my_df3])) # tabloları alt alta birleştir

# merge
print(pd.merge(my_df1, my_df2, on="Sports")) # Sports sütununu ortak sütun yapar, diğer sütunlara "_x, _y" ön ekleri ekleyerek birleştirir

# unique değerler
new_salary_frame = pd.DataFrame({"Name" : ["James","Kirk","Lars"], "Salary" : [10,20,30], "Age" : [60,65,70]})
print(new_salary_frame["Name"].unique()) # Name sütunundaki eşsiz değerler
print(new_salary_frame["Name"].nunique()) # Name sütunundaki eşsiz değerlerin adedi

# fonksiyonları df üzerinde çalıştırmak
def grossNet(salary):
    return salary * 0.65
print(new_salary_frame["Salary"].apply(grossNet))