s = int(input("masukkan sisi persegi : "))
y = input("hitung luas/keliling : ").lower()

pilihan = ["keliling", "luas"]
hasil = [4 * s, s * s]
pesan = "Oops, hanya bisa input \"luas\" atau \"keliling\". Periksa kembali input-an Anda"

print(dict(zip(pilihan, hasil)).get(y, pesan))
      # gunanya zip untuk memasangkan dua elemen dari dua list yang berbeda
