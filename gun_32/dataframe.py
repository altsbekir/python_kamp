import pandas as pd
import numpy as np

my_data = np.array([[10, 20, 30], [15, 25, 35], [30, 40, 50], [45, 35, 20]])
print(my_data) # bildiğimiz numpy matris'i
# veriyi dataframe yapısına dönüştürmek
my_names = ["James", "Lars", "Kirk", "Rob"] # satırlar
my_columns = ["Jan", "Feb", "Mar"] # sütunlar
my_data_frame = pd.DataFrame(my_data)
print(my_data_frame) # indeksleri kendisinin verdiği tablo oluşur
new_data_frame = pd.DataFrame(my_data, index=my_names, columns=my_columns) # kendi isimlendirmelerimizi veriyoruz
print(new_data_frame)

# sütuna indeks mantığıyla erişmek
print(new_data_frame["Feb"])
print(type(new_data_frame["Feb"])) # tipi series'tir

# birkaç operasyon
feb_series = new_data_frame["Feb"]
print(feb_series.mean()) # ortalama
print(feb_series.Lars) # bir satırın verisi çekmek
print(feb_series["Lars"]) # bu şekilde de satırların verisine erişilinebilir
print(feb_series.max()) # sütundaki maksimum değer
print(new_data_frame[["Jan","Feb"]]) # sadece seçilen iki sütunu aldık
print(new_data_frame.loc["Lars"]) # satırlara erişmek
print(new_data_frame.loc["Lars"].mean()) # örnek: Lars'ın ortalama maaşı
print(new_data_frame.iloc[3]) # satırlara indeksle erişmek

# örnek: nisan ayında kazanılan maaş her çalışan için mart ayının 2 katı olsun
# bunu df'ye nasıl ekleriz?
new_data_frame["Apr"] = new_data_frame["Mar"] * 2
print(new_data_frame)

# drop
# axis = 0 -> satırlar, axis = 1 -> sütunlar
print(new_data_frame.drop("Rob", axis=0)) # yeni df oluşturur, var olanın üzerinde işlem yapmaz
print(new_data_frame.drop("Apr", axis=1))
print(new_data_frame) # eskisinin bozulmadığını görebiliriz
new_data_frame.drop("Apr", axis=1, inplace=True) # var olan df'de düşürmek için
print(new_data_frame)

# boolean işlemler
boolean_frame = new_data_frame > 25
print(boolean_frame) # true-false'dan oluşan bir df
# şarta uyan verileri tutmak istersek
print(new_data_frame[boolean_frame]) # şartı sağlamayanlar nan olur
# pratik olarak şöyle yapılablir
print(new_data_frame[new_data_frame > 25])

# örnek: mart ayında maaşı 25'ten fazla olanlar df'de kalsın
print(new_data_frame[new_data_frame["Mar"] > 25])

# indeks sıfırlama - değiştirme
print(new_data_frame.reset_index()) # mevcut df'yi bozmaz
new_data_frame["NewIndex"] = ["Jam", "Lar", "Kir", "Rob"] # yeni indeks isimlerini sütun olarak oluşturduk
print(new_data_frame.set_index("NewIndex")) # indeks sütunumuzu kullanarak indeks isimlerini güncelledik
new_data_frame.drop("NewIndex", axis=1, inplace=True)