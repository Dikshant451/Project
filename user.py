def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful.")
                return
    print("Invalid username or password.")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

