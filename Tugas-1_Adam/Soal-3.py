#3.	Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
    #Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal.
    #Jika nilai ujian teori dan praktek minimal 70,  maka program akan menampilkan:
    #Jika nilai ujian teori minimal 70 dan nilai ujian praktek kurang dari 70:
    #Jika nilai ujian teori kurang dari 70 dan nilai ujian praktek minimal 70:
    #Jika nilai ujian teori dan ujian praktek kurang dari 70:

print("Selamat datang di sistem prediksi kelulusan ujian")
a = float(input("Masukkan nilai ujian teori:"))
b = float(input("Masukkan nilai ujian praktik:"))
c = float(70)
if a>=c and b>=c:
    print("Selamat, anda lulus!")
if a>=c and b<c:
    print("Anda harus mengulang ujian praktek.")
if a<c and b>=c:
    print("Anda harus mengulang ujian teori.")
if a<c and b<c:
    print("Anda harus mengulang ujian teori dan praktek.")