class Induk(object):
    def __init__(self, hewan, warna, berat, kelamin) :
        self.hewan = hewan
        self.warna = warna
        self.berat = berat
        self.kelamin = kelamin
    
    def Bernafas(self):
        print("Bernafas menggunakan paru - paru")
        
    def BerkembangBiak(self):
        print("Berkembang biak dengan bertelur")
        
    def lahir(self):
        print("Saya baru lahir dengan cara menetas dari telur")
        
class Anak(Induk):
     pass
     
b = Induk("Ayam", "Putih", 4, "Betina")
print()
print("INDUK")
print("Hewan:", b.hewan)
print("Warna:", b.warna)
print("Berat:", b.berat, "kg")
print("Kelamin:", b.kelamin)
b.Bernafas()
print("Dan")
b.BerkembangBiak()

#Objek dari class anak

a = Anak("Ayam", "coklat", 0.3, "Jantan")
print()
print("ANAK")
print("Hewan:", a.hewan)
print("Warna:", a.warna)
print("Berat:", a.berat, "kg")
print("Kelamin:", a.kelamin)
a.lahir()
print("Dan")
a.Bernafas()
