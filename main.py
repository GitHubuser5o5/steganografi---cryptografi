import numpy as np
from PIL import Image


def text_to_bits(text):
    #lav tekst om til et array af bits
    text_in_bytes = text.encode("utf-8")
    text_byte_array = np.frombuffer(text_in_bytes, dtype=np.uint8)
    return np.unpackbits(text_byte_array)

def bits_to_text(bits):
    #lav et array af bits om til tekst
    text_byte_array = np.packbits(bits)
    text_in_bytes = text_byte_array.tobytes()
    return text_in_bytes.decode("utf-8")

def rgb_img_to_array(img):
    #convertere billed til array, kun med RGB
    img = img.convert("RGB")
    return np.array(img)


if __name__ == "__main__":
    text = "hi"
    print(text_to_bits(text))
    
    print("")

    bits = text_to_bits(text)
    print(bits_to_text(bits))

    print("")

    img = Image.open("California_quail.png")
    print(rgb_img_to_array(img).shape)