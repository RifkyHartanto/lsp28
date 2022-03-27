def garis():
    print("-------------------------------")

#Fungsi Bubble Sort Ascending(Dari kecil ke besar)
def sort_asc(array):
    array = sorted(array)
    return(array)

#fungsi bubble sort descending (Dari besar ke kecil)
def sort_desc(array):
    array = sorted(array, reverse = True)
    return(array)

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
print("-----HASIL AKHIR------")
print("Urutan angka ascending : ",(sort_asc(angka)))
print("Urutan angka descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka terbesar : ", max(angka))

#angka terkecil
print("Angka terkecil : ", min(angka))

#rata rata
print("Rata ratanya : ", round(rata_rata(angka),2))
