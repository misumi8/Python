# Probleme usoare:
# 1 -----------------------------------

with open("olimpice.py", "r") as f:
    prop = f.read()

freq = {}
for letter in "abcdefghijklmnopqrstuvwxyz":
    freq[letter] = prop.count(letter)
maxFreq = max(freq.values())
m = []
for i in range(26):
    m += ['o' * freq[chr(ord('a') + i)] + '.' * (maxFreq - freq[chr(ord('a') + i)])]

# for j in range(maxFreq):
#     for i in range(26):
#         print(m[i][maxFreq - j - 1], end = "")
#     print("", maxFreq - j)
# print(''.join(freq.keys()))

# 2 --------------------------------

tuples = [(letter, ord(letter), 25 - index) for index, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
# for i in tuples:
#     print(i)

# 3 --------------------------------

with open("olimpice.py", "r") as f:
    text = f.read()

hexRepresentation = [[]]
hexAlphabet = "0123456789ABCDEF"
hexRepresentation[0].append("         ")
hexRepresentation.append([])
hexRepresentation[1].append("       +------------------------------------------------")
for i in range(0, 16):
    hexRepresentation[0].append("0" + hexAlphabet[i] + " ")

count = 0
j = 2
hexRepresentation.append([str(count).zfill(4) + "   | "])
for i in range(0, len(text)):
    hexRepresentation[j].append(str(hex(ord(text[i])).removeprefix("0x").upper().zfill(2) + " "))
    if((i+1) % 16 == 0 and i < len(text) - 1):
        j += 1
        count += 10
        hexRepresentation.append([str(count).zfill(4) + "   | "])

# for ln in hexRepresentation:
#     print("".join(ln))

# 4 --------------------------------

def getBinaryMatrix(list):
    if(len(list) != 16):
        raise Exception("List length must be equal to 16")
    binMatrix = []
    for i in range(0, len(list)):
        binMatrix.append(bin(list[i]).removeprefix("0b").zfill(8))
    return binMatrix

def writeMatricesToFile(lists):
    matrices = []
    for list in lists:
        matrices.append(getBinaryMatrix(list))
    with open("matrices.txt", "w") as f:
        for i in range(0, len(matrices[1])):
            for matrix in matrices:
                f.write(matrix[i])
            f.write("\n")

lists = [[0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
    [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]]
writeMatricesToFile(lists)