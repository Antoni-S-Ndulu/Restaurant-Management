import pymysql as p 
import qrcodeModule as q

#establishing connection to the database
conn = p.connect(host='localhost', user='root', 
                 password='1240', database='restaurantDB',
                 port=3306,
                 cursorclass=p.cursors.DictCursor)


def view_foods():
        #establishing connection to the database
    foodSQL = "SELECT foodname, foodprice FROM food;"
    cursor = conn.cursor()
    cursor.execute(foodSQL)

    #loop to view food
    for row in cursor.fetchall():
          print(f"Food Name: {row['foodname']}, Price: {row['foodprice']}")

#view_foods()


def order_food(foodname, quantity):
    #establishing connection to the database
    orderSQL = "SELECT foodID FROM food WHERE foodname = %s;"
    cursor = conn.cursor()
    cursor.execute(orderSQL, (foodname))
    foodID = cursor.fetchone()['foodID']

    #getting customerID from user input
    user = input("Enter your first name: ")
    user2 = input("Enter your last name: ")
    namesql = "SELECT customerID FROM customer WHERE firstname = %s AND lastname = %s;"
    cursor.execute(namesql, (user, user2))
    customerID = cursor.fetchone()['customerID']

    #establish transaction
    #including verification_token from qrcodeModule.py
    token = q.generate_secret()
    transSQL = "INSERT INTO transaction(quantity, foodID,  customerID,token ) VALUES (%s, %s, %s, %s);"
    cursor.execute(transSQL,(quantity, foodID, customerID,token))
    conn.commit()

    #print token to qr code
    q.print_token_toQRcode(token)

    #getting total price of ordered food
    totalSQL = "SELECT foodprice from food where foodID = %s"
    cursor.execute(totalSQL, foodID)
    price =cursor.fetchone()['foodprice']
    totalprice = price * quantity
    print(f"Order placed for {quantity} of {foodname}.")
    print("Total Price is ", totalprice)



view_foods()
fname = input('Enter name of food: ')
fprice = int(input('Enter price of one food: '))
order_food(fname, fprice)

#qr code for your token is