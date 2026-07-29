import pymysql as p
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()
con = p.connect(
    user='root',
    password='1240',
    host='localhost',
    port=3306,
    database='RestaurantDB',
    cursorclass=p.cursors.DictCursor
)


#retrieving user data from database
hashedSQL = 'SELECT password FROM customer WHERE firstname = %s AND lastname = %s'


#acceptb user name and password from user
username1 = input("Enter your first name: ")
username2 = input("Enter your last name: ")
toVerifyPassword = input("Enter your password: ")

#initializing cursoer
cursor = con.cursor()
cursor.execute(hashedSQL, (username1, username2))
result = cursor.fetchone()

try:
    #verify password using argon2
    ph.verify(result['password'], toVerifyPassword)
    print("Password verified successfully!")
except VerifyMismatchError:
    print("Invalid username or password.")  

except Exception as e:
    print("An error occurred:", str(e))