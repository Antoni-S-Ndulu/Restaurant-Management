import pymysql as p
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize hasher
ph = PasswordHasher()

def get_db_connection():
    """Establishes and returns a database connection."""
    return p.connect(
        user='root',
        password='1240',
        host='localhost',
        port=3306,
        database='RestaurantDB',
        cursorclass=p.cursors.DictCursor
    )

def get_hashed_password(cursor, first_name, last_name):
    """Retrieves the hashed password for a specific user."""
    sql = 'SELECT password FROM customer WHERE firstname = %s AND lastname = %s'
    cursor.execute(sql, (first_name, last_name))
    result = cursor.fetchone()
    
    # Return the password string if found, otherwise return None
    return result['password'] if result else None

def verify_user_login(first_name, last_name, plain_password):
    """Handles the full login logic."""
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            stored_hash = get_hashed_password(cursor, first_name, last_name)
            
            if stored_hash is None:
                print("User not found.")
                return False
            
            else:
                # Verify password
                            ph.verify(stored_hash, plain_password)
                            print("Password verified successfully!")
                            return True
            
    except VerifyMismatchError:
        print("Invalid username or password.")
        return False
    except Exception as e:
        print("An error occurred:", str(e))
        return False
    finally:
        if connection:
            connection.close()

    