import pymysql as p

con = p.connect(
    user='root',
    password='1240',
    host='localhost',
    port=3306,
    cursorclass=p.cursors.DictCursor
)

#registration module
def register_user( ):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    cs = con.cursor()
    cs.execute('USE restaurantDB;')
    q1 = 'INSERT INTO customer (name, password) VALUES (%s, %s)'
    cs.execute(q1, (name, password))
    con.commit()
    cs.close()