def garis():
    print("-------------------------------")

#Fungsi Bubble Sort Ascending(Dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (Dari besar ke kecil)
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#input nilai
garis()
print("Masukan tiga buah nilai")
nilai_a = int(input("Nilai A : "))
nilai_b = int(input("Nilai B : "))
nilai_c = int(input("Nilai C : "))
angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#nilai akhir
print("HASIL AKHIR------")
print("Urutan angka ascending : ",(sort_asc(angka)))
print("Urutan angka descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka terbesar : ", max(angka))

#angka terkecil
print("Angka terkecil : ", min(angka))

#rata rata
print("Rata ratanya : ", round(rata_rata(angka),2))
