#dosya oluşturmak
myFile = open("myFile.txt","w")
print(type(myFile))

#yazmak - open("","w")'den sonra
myFile.write("test 1\ntest 2\ntest 3")
myFile.close() #kapatıyoruz

#okumak
myFile = open("myFile.txt","r")
print(myFile.read())

#tekrar okursak boş çıkacaktır, çünkü imleç gibi en sona gelmiştir
print(myFile.read())
#bunu engellemek için dosyanın en başına şu şekilde gitmeliyiz:
myFile.seek(0)
print(myFile.read())

#dosyayla çalıştığımız zaman dosyayı kapatmamız da önemlidir
myFile.close()

#with keyword'ü
with open("myFile.txt") as myFile:
    myContent = myFile.read()
#artık defalarca okumak imleci sona getirmeyecek
print(myContent)
print(myContent)
print(myContent)
#not: dosya kapatma işlemini de otomatik olarak yapar

#"w" mode'u dosya içeriğini silip baştan yazdırır
with open("myFile.txt", mode="w") as myNewFile:
    myNewFile.write("test 4")
with open("myFile.txt", mode="r") as myNewFile2:
    myContent = myNewFile2.read()
print(myContent)

#"a" (append) mode'u
with open("myFile.txt", mode="a") as myNewFile3:
    myNewFile3.write("\ntest 5")
with open("myFile.txt", mode="r") as myNewFile4:
    myContent = myNewFile4.read()
print(myContent)