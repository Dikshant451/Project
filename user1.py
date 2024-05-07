# Sample user database (for demonstration purposes)
user_database = {
    'tanmay': 'tanmay1324',
    'user2': 'password2',
    'user3': 'password3'
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username exists in the database
    if username in user_database:
        # Verify the entered password
        if user_database[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register.")

def register():
    username = input("Enter a new username: ")

    # Check if the username already exists
    if username in user_database:
        print("Username already exists. Please choose a different username.")
    else:
        password = input("Enter a password: ")
        user_database[username] = password
        print("Registration successful!")

def main():
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
