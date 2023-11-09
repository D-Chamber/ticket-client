import requests

# Server URL
SERVER_URL = 'http://127.0.0.1:5000'  # Change to your server's URL


def register_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f'{SERVER_URL}/register', json=data)
    return response.json()


def login_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f'{SERVER_URL}/login', json=data)
    return response.json()


def check_available_tickets():
    # Add code to request available ticket information from the server
    pass


def check_owned_tickets(username):
    # Add code to request owned ticket information for the given user from the server
    pass


def buy_tickets(username, event, quantity):
    # Add code to request purchasing tickets from the server
    pass


def main():
    logged_in = False

    while True:
        if not logged_in:
            print("1. Register")
            print("2. Login")
        else:
            print("3. Check Available Tickets")
            print("4. Check Owned Tickets")
            print("5. Buy Tickets")
            print("6. Logout")

        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            result = register_user(username, password)
            print(result["message"])

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            result = login_user(username, password)
            if "message" in result:
                print(result["message"])
                if "points" in result:
                    print(f"Points: {result['points']}")
                    logged_in = True
            else:
                logged_in = False

        elif choice == '3' and logged_in:
            check_available_tickets()
            # Implement code to display available tickets

        elif choice == '4' and logged_in:
            username = input("Enter your username: ")
            check_owned_tickets(username)
            # Implement code to display owned tickets for the user

        elif choice == '5' and logged_in:
            username = input("Enter your username: ")
            event = input("Enter the event name: ")
            quantity = int(input("Enter the quantity: "))
            buy_tickets(username, event, quantity)
            # Implement code to purchase tickets

        elif choice == '6':
            logged_in = False

        elif choice == '7':
            break


if __name__ == '__main__':
    main()