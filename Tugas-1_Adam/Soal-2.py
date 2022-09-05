#2.	Buatlah sebuah program yang dapat menghitung luas lingkaran.
    #Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
    #Program menghitung luas lingkaran dengan rumus πr² 
    #Π = 22/7
    #r = jari - jari lingkaran 
    #Lalu tampilkan ke layar dengan format:
    #Hint: untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)

print("Selamat datang di kalkulator luas lingkaran")
jari = int(input("Tuliskan jari-jari lingkaran:"))
luas = 22/7*(jari)**2
text = 'Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2'.format(jari,luas)

print(text)