import orderModule as o

# Import modules (Ideally place these at the top of your file)
import verifyUserModule as v
import registrationModule as reg


def get_food_name():
    return input("Enter the name of the food you want to order: ")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity of the food you want to order: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def login_or_register():
    """Returns True if the user successfully logs in or registers."""
    while True:
        choice = input("Do you want to login or register? (login/register): ").strip().lower()
        
        if choice == "login":
            # We assume v.main() returns True on success, False otherwise
            if v.verify_user_login(input("Enter your first name: "), 
                                   input("Enter your last name: "), input("Enter your password: ")):  
                print("Login successful!")
                return True 
            else:
                print("Login failed. Please try again.")
        
        elif choice == "register":
            # We assume reg.register_user() returns True on success
            if reg.register_user(): 
                print("Registration successful!")
                return True
            else:
                print("Registration failed.")
        
        else:
            print("Invalid choice. Please enter 'login' or 'register'.")

def main():
    # 1. Attempt to authenticate
    print("Welcome! Please authenticate to order food.")
    is_authenticated = login_or_register()

    # 2. Only proceed if authentication returned True
    if is_authenticated:
        print("\n--- Proceeding to Order ---")
        o.view_foods()
        o.order_food(foodname=get_food_name(), quantity=get_quantity())
    else:
        print("Access denied. Could not verify or register user.")

if __name__ == "__main__":
    main()