import pymysql as p 

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

view_foods()


def order_food(foodname, quantity):
    #establishing connection to the database
    orderSQL = "SELECT foodID FROM food WHERE foodname = %s;"
    cursor = conn.cursor()
    cursor.execute(orderSQL, (foodname))
    foodID = cursor.fetchone()['foodID']

    #establish transaction
    transSQL = "INSERT INTO transaction(quantity, foodID ) VALUES (%s, %s);"
    cursor.execute(transSQL,(quantity, foodID))
    conn.commit()

    
    #getting total price of ordered food
    totalSQL = "SELECT foodprice from food where foodID = %s"
    cursor.execute(totalSQL, foodID)
    price =cursor.fetchone()['foodprice']
    totalprice = price * quantity
    print(f"Order placed for {quantity} of {foodname}.")
    print("Total Price is ", totalprice)

namef = input("Enter Name of food: ")
q = int(input("Enter quantity of food: "))
order_food(namef, q)

     