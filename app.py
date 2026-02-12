import hashlib


def login(username, password):
    # insecure hardcoded credentials
    if username == "admin" and password == "123456":
        print("Login successful")
    else:
        print("Login failed")


def hash_password(password):
    # outdated hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()


user_input = input("Enter your age: ")
age = int(user_input)

print("Your hashed password:", hash_password("mypassword"))
