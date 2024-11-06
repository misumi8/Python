# 1 --------------------------------------------------
import struct

def transform_to_ascii(bmp_img):
    with open(bmp_img, "rb") as f:
        chars = "!@#$%^&*()_*-+,./';[]\<>?:{}|~` "
        data = f.read(14)
        # I - int, H - short, < - little endian
        header = struct.unpack("<2sIHHI", data)
        dib_header = f.read(40)
        dib_header_unpacked = struct.unpack("<IIIHHIIIIII", dib_header)
        image_size = dib_header_unpacked[6]
        f.seek(header[4])
        pixel_array = f.read(image_size)
        ascii_bmp = ""
        row_size_no_padd = dib_header_unpacked[1] * 3
        # calculating row size without padding
        while(row_size_no_padd % 4 != 0):
            row_size_no_padd += 1
        for i in range(dib_header_unpacked[2] - 1, -1, -1): # start, stop, step
            for j in range(0, dib_header_unpacked[1]): # width
                # i * row_size_no_padd row
                pos = i * row_size_no_padd + (j * 3)
                # 24 bits, 3 bytes
                char = (pixel_array[pos] + pixel_array[pos + 1] + pixel_array[pos + 2]) // 3
                ascii_bmp += chars[char * len(chars) // 256] + " "
            ascii_bmp += "\n"
        return ascii_bmp

files = ["alien", "earth", "heart", "mouse", "Spidey", "stars", "tree"]
for file in files:
    with open("ascii_bmp/" + file + ".txt", "w") as f:
        f.write(transform_to_ascii("ImaginiBmp/" + file + ".bmp"))
