import pandas as pd
import numpy as np

df = pd.read_excel("gun_32/27-SalarySheet.xlsx")
print(df)

# 1) Toplamda kaç satır veri vardır?
print(df.count()) # her sütunda 100 satır veri var
print(len(df)) # doğrudan toplam satır sayısını döndürür, en yüksek performans ve temiz kod için ideal
print(df.index.size) # indeks sayısını döndüren başka bir yöntem

# 2) Bu firma ortalama ne kadar maaş vermektedir?
print(df["Salary"].mean()) # cevap: 725.84

# 3) Bu firmada departmanlara göre ortalama maaş karşılaştırması nasıldır?
groupdpt = df.groupby("Department")
print(groupdpt["Salary"].mean()) # Salary'e özel bakış
print(groupdpt.mean(numeric_only=True)) # sayısallara geneş bakış
print(groupdpt["Salary"].mean().to_list()) # listeye çevirmek
print(groupdpt["Salary"].mean().to_dict()) # sözlüğe çevirmek

# 4) Bu firmada title (senior - junior) durumuna göre ortalama maaş karşılaştırması nasıldır?
group_title = df.groupby("Title")
print(group_title["Salary"].mean()) # departmandaki mantığın aynısı geçerli

# 5) Senior bir kişinin junior bir kişiye göre maaşı ortalama yüzde kaç fazladır?
title_dict = group_title["Salary"].mean().to_dict()
print(f"Senior bir kişinin junior birine göre maaşı %{((title_dict["Senior"] - title_dict["Junior"]) / title_dict["Junior"]) * 100} fazladır.")

# 6) Software Development departmanında senior bir kişinin junior bir kişiye göre maaşı ortalama ne kadar fazladır?
software_df = groupdpt.get_group("Software Development")
software_group = software_df.groupby("Title")
software_title_dict = software_group["Salary"].mean().to_dict()
print(f"SD'de senior birinin junior birine göre maaşı ortalama {software_title_dict["Senior"] - software_title_dict["Junior"]} fazladır.")

# 7) Finance departmanında c-level bir kişinin mid-senior bir kişiye göre maaşı ortalama ne kadar fazladır?
finance_df = groupdpt.get_group("Finance")
finance_group = finance_df.groupby("Title")
finance_title_dict = finance_group["Salary"].mean().to_dict()
print(f"Finance'da C-level birinin Mid-Senior birine göre maaşı ortalama {finance_title_dict["C-level"] - finance_title_dict["Mid-Senior"]} fazladır.")

# 8) Software development departmanında c-level çalışan sayısı marketing departmanında çalışana oranla kaç kat fazladır?
sd_clevel = software_df["Title"].value_counts().to_dict()["C-level"]
marketing_df = groupdpt.get_group("Marketing") # marketing df'yi hazırlayalım
marketing_clevel = marketing_df["Title"].value_counts().to_dict()["C-level"]
print(f"SD'de C-level çalışan sayısı marketing'dekilerin yaklaşık {int(sd_clevel/marketing_clevel)} katıdır.")