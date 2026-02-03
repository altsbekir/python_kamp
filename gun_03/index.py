#index saymaya 0'dan başlanır
my_string = "zehra bekir"
print(my_string[4])

#len-1 işlemi her durumda son index'i verir
print(my_string[len(my_string)-1])

#python'a özel olarak -1 de son index'i verir
print(my_string[-1])

#-1 den geriye doğru sayarak sondan geriye doğru diğer indexler de bulunabilir
print(my_string[-2])
print(my_string[-3])

#SLICING NEDİR?

#python'da stringler de toplanabilir ama çıkartılamaz
print("A" + "B")
name = "bekir"
surname = "alatas"
full_name = name + " " + surname
print(full_name)

#stringler çarpılabilir ama bölünemez
print(full_name * 3)

#barkod örneği
barcode = "ABCDE123456789"
print(barcode[0] + barcode[1] + barcode[2])
#bu işlem daha kısa yollarla yapılabilir

#slicing, starting index, stopping index, stepping size
print(barcode[::])

#barcode[starting index: stopping index: stepping size] şeklinde yazıyoruz
print(barcode[3::])
print(barcode[:3:])
print(barcode[::2])

#stepping size -1 olursa tersten yazdırır
print(barcode[::-1])

#name.index ile harfin bulunduğu index'i bulabiliriz
print(name.index("k"))

#name.split ile stringi ayırabiliriz (rastgele)
print(full_name.split())

#name.split'in türü list'tir
print(type(full_name.split()))