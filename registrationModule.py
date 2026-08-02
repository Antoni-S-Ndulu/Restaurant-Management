import pymysql as p
from argon2 import PasswordHasher

con = p.connect(
    user='root',
    password='1240',
    host='localhost',
    port=3306,
    database='RestaurantDB',
    cursorclass=p.cursors.DictCursor
)

#registration module
def register_user( ):
    fname = input("Enter your first name: ")
    lname = input('Enter your last name: ')
    bill = int(input('Enter your bill to place: '))
    password = input("Enter your password: ")

    #hashing using argon2
    ph = PasswordHasher()
    hashedPassword = ph.hash(password)

#initialize cursor
    cs = con.cursor()
   
    q1 = 'INSERT INTO customer (firstname,lastname, password, Bill) VALUES (%s, %s, %s, %s)'
    cs.execute(q1, (fname,lname, hashedPassword, bill))
    con.commit()
    cs.close()
#register_user()
con.close()