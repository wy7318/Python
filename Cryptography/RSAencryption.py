class RsaEncryption:

    def __init__(self, message, p, q, e):
        self.message = message
        self.p = p
        self.q = q
        self.e = e
        print("You have typed '{}' with RSA key n = {}, e = {}".format(message, p^q, e))
        self.encryption()

    def char_num(self):                                                  #Convert character into number with RSA table
        res = ""
        for i in range(0, len(self.message)):           
            if ord(self.message[i].lower())-96 <=9:                      #if converted number is less than 9, we should put 0 in front
                res = res + "0" + str(ord(self.message[i].lower())-96)
            else:
                res = res + str(ord(self.message[i].lower())-96)
        return int(res)

    def encryption(self):
        encrypt = (self.char_num()**self.e)%(self.p*self.q)
        print("Your Encrypted message is {}".format(encrypt))


RsaEncryption("hi", 67, 131, 4903)
