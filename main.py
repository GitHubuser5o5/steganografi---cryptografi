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

def embed_bits(img, text):
    #embedder bits fra text i billedets LSB
    flat_img_array = rgb_img_to_array(img).reshape(-1)
    text_bits = text_to_bits(text)
    n = len(text_bits)
    valgte_pixels = flat_img_array[:n]
    ryddet_lsb_pixels = valgte_pixels & 0xFE
    nyt = ryddet_lsb_pixels | text_bits
    flat_img_array[:n] = nyt
    return flat_img_array.reshape(rgb_img_to_array(img).shape)

def save_embedded_img(new_img):
    result = Image.fromarray(new_img)
    result.save("result.png")
    return 1

def check_input_against_img(img, text):
    text_bit_length = len(text_to_bits(text))
    img_bit_length = rgb_img_to_array(img).size
    if(text_bit_length > img_bit_length):
        print("image too small for input text")
        raise ValueError("image too small for input text")

##test box
if __name__ == "__main__":
    text = "hi"
    print(text_to_bits(text))
    
    print("")

    bits = text_to_bits(text)
    print(bits_to_text(bits))

    print("")

    img = Image.open("California_quail.png")
    print(rgb_img_to_array(img).shape)

    print("")

    save_embedded_img(embed_bits(img, text))
    print(rgb_img_to_array(Image.open("result.png")).reshape(-1)[:16])
