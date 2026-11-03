x = 20
print(x, bin(x))

#ændre sidste bit til 0
ryddet = x & 0xFE
print(ryddet, bin(ryddet))

#ændre sidste bit til 1
med_en = ryddet | 1
print(med_en, bin(med_en))

#sidste bit forbliver uændret
med_nul = ryddet | 0
print(med_nul, bin(med_nul))




from PIL import Image
import numpy as np

##billede

#åbner filen
img = Image.open("California_quail.png")

#aflæses som RGB farver så der ikke er gennemsigtighed
img = img.convert("RGB")

#laver billedet om til et array af tal
arr = np.array(img)

print(arr.shape)
print(arr[0,0])
print(arr.dtype)



##teksten encode

#printer beskeden og dens bytes
print()
message = "hi"
msgbytes = message.encode("utf-8")
print(msgbytes)
print(list(msgbytes))

#sætter alle bytes som en lang string
arr_bytes = np.frombuffer(msgbytes, dtype=np.uint8)
print(arr_bytes)

#laver bytes om til bits
bits = np.unpackbits(arr_bytes)
print(bits)


##teksten decode
print()

#tekst til bits
packed = np.packbits(bits)
print(packed)

#bites til bytes
raw = packed.tobytes()
print(raw)

#bytes til string
text = raw.decode("utf-8")
print(text)