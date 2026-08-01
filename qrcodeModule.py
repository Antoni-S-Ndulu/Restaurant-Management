import qrcode
import pymysql as p
#import orderModule as o
import secrets as s
# secrets module to generate food authentication string in restaurant


# generate
def generate_secret():
    token = s.token_hex(16)
    return token


    


def get_random():
    rnd = s.randbelow(1000)
    return rnd



def print_token_toQRcode(token):
    #token = generate_secret()
    img = qrcode.make(token)
    type(img)

    savestring = str(get_random())
    #put transactionID
    img.save(f"save{savestring}.png")
#print_token_toQRcode()

