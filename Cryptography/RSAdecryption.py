import math

class RsaDecryption:

    def __init__(self, cipher, n, e):
        self.cipher = cipher
        self.n = n
        self.e = e
        print("Cipher text '{}' with key (n, e) = ({}, {})".format(cipher, n, e))
        self.decryption()

    def fermatp(self):
        for x in range(1,10000):
            y = self.n + x**2
            if math.sqrt(y) % 1 == 0:
                p = int(math.sqrt(y)) + x
                return p

    def fermatq(self):
        for x in range(1,10000):
            y = self.n + x**2
            if math.sqrt(y) % 1 == 0:
                q = int(math.sqrt(y)) - x
                return q

    def getd(self):
        for d in range(1, (self.fermatp()-1)*(self.fermatq()-1)):
            if (self.e*d) % ((self.fermatp()-1)*(self.fermatq()-1)) == 1:
                return int(d)

    def plainNumber(self):
        plainN = int((self.cipher**self.getd()) % self.n)
        return plainN

    def chunk(self, my_list):
        final = [my_list[i * 2:(i + 1) * 2] for i in range((len(my_list) + 2 - 1) // 2 )]
        return final

    def decryption(self):
        res = ""
        res1 = ""
        for i in range(0, len(str(self.plainNumber()))//2):
            if len(str(self.plainNumber())) % 2 == 0:
                res = res + chr(int(self.chunk(str(self.plainNumber()))[i]) + 96)
            else:
                res1 = chr(int(str(self.plainNumber())[0])+96)
                res = res + chr(int(self.chunk(str(self.plainNumber()))[1:][i])+96)
        print("Your decryption for ciphertext {} is '{}'".format(self.cipher, res1 + res))


RsaDecryption(1660, 8777, 4903)
