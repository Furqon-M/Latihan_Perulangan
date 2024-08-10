# Latihan perulangan membuat segitiga

sisi = 9

# 1. MENGGUNAKAN FOR
# dummy variable
print("AWAL DARI FOR\n")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1


# 2. MENGGUNAKAN WHILE
print("\nAWAL DARI WHILE\n")
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break

# 3. HANYA GANJIL SAJA

print("\nAWAL DARI GANJIL\n")
count = 1
while True:
    # akan kembali ke atas jika ganjil
    if count%2:
        #print jika ganjil
        print("*"*count)
        count += 1
    else:
        #akan kembali ke atas jika ganjil
        count += 1
        continue
   
    # akan break jika count melebihi sisi
    if count > sisi:
        break

# 4. HANYA GANJIL SAJA

print("\nAWAL DARI GANJIL SAJA\n")
count = 1
spasi = int(sisi/2)
while True:
    # akan kembali ke atas jika ganjil
    if count%2:
        #print jika ganjil
        print(" "*spasi,"+"*count) 
        spasi -= 1
        count += 1
    else:
        #akan kembali ke atas jika ganjil
        count += 1
        continue
   
    # akan break jika count melebihi sisi
    if count > sisi:
        break

# 5. HANYA GANJIL SAJA MEMBUAT POLA KETUPAT

print("\nKETUPAT\n")

spasi = int(sisi / 2)
count = 1
# membuat segitiga atas
while count <= sisi:
    if count % 2 == 1:
        print(" " * spasi, "*" * count)
        spasi -= 1
    count += 1

# buat segitiga bawah

spasi = 1
count = sisi - 2
while count >= 1:
    if count % 2 == 1:
        print(" " * spasi, "*" * count)
        spasi += 1
    count -= 1    