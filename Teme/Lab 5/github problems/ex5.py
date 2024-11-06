# 5 --------------------------------------------------
import zlib
import pyzipper

class PRNG:
    def __init__(self, seed = 327680):
        self.seed = seed
        self.a = 4291010243
        self.c = 179203

    def random(self):
        self.seed = (self.a - self.seed * self.c) % 16777216
        rnd = self.seed / 16777216
        return rnd

alfabet = "9876543210qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
# brute force
with pyzipper.AESZipFile("arhiva.zip") as zf:
    i = 0
    while(True):
        try:
            rand = PRNG(i)
            passw = "".join([alfabet[int(rand.random() * 100) % len(alfabet)] for i in range(64)])
            zf.setpassword(passw.encode())
            zf.extractall(path="arhiva")
            print("[Correct password]", passw)
            break
        except RuntimeError:
            print("[Wrong password]", passw)
            i += 1
        except Exception as e:
            print(e.__str__())
            i += 1
