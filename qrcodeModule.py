import qrcode
import pymysql as p
import orderModule as o
import secrets as s
# secrets module to generate food authentication string in restaurant


# generate
def generate_secret():
    token = s.token_hex(16)
    return token


# store in both databases
def tokenToDatabase():
    #establish connecion
    cn = p.connect(
        host='localhost',
        database='RestaurantDB',
        port=3306,
        user='root',
        password='1240',
        cursorclass=p.cursors.DictCursor
    )


#get customer name to get customerid
    name = input('Enter your firstname: ')
    name2 = input('Enter your lasttname: ')
    namecode = 'SELECT customerid FROM customer WHERE firstname = %s AND lastname = %s'
    token = generate_secret()

    #get transactin to get its id
    #insert values into transactions
    #token_sql ='INSERT INTO customer(customerqrfood) VALUES (%s);'
    #token_sql2 ='INSERT INTO manager(token) VALUES (%s);'  put trigger to automatically into manager table
    cursor = cn.cursor()
    cursor.execute(token_sql, (token))
    cursor.execute(token_sql2, (token))
    cn.commit()
    cursor.close()
    cn.close()


def get_random():
    rnd = s.randbelow(1000)
    return rnd

def print_token_toQRcode():
    token = generate_secret()
    img = qrcode.make(token)
    type(img)

    savestring = str(get_random())
    #put transactionID
    img.save(f"save{savestring}.png")
print_token_toQRcode()

o.view_foods()
namef = input('Enter name of food: ')
price = int(input('Enter price of one food: '))

o.order_food(namef, price)