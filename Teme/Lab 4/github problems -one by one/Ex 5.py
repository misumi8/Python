# 5 ---------------------------------------------------
from pprint import pprint
import struct

def bmp_text_form(bmp):
    with open(bmp, "rb") as f:
        data = f.read(14)
        # I - int, H - short, < - little endian
        header = struct.unpack("<2sIHHI", data)
        print("File size:", header[1])

        dib_header = f.read(40)
        dib_header_unpacked = struct.unpack("<IIIHHIIIIII", dib_header)
        print("Image width (pixel):", dib_header_unpacked[1])
        print("Image height (pixel):", dib_header_unpacked[2])
        print("Bits per pixel:", dib_header_unpacked[4])
        print("Image size:", dib_header_unpacked[6])

        print("\nImage data (1%): ")
        image_size = dib_header_unpacked[6]
        # move cursor to header[3] bytes
        f.seek(header[3])
        pixel_array = f.read(image_size // 100)
        pprint(" ".join([hex(byte).removeprefix("0x").zfill(2).upper() for byte in pixel_array]))

# bmp_text_form("python.bmp")
