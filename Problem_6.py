#login for student management system and add unique thing to ensure security > security question

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "123":
        print("Before the login in Student Management System write answer for this security question.")
        while True:
            security_answer = input("What is your favorite color? ")
            if security_answer.lower() == "blue":
                print("Login successful! Welcome to the Student Management System.")
                break
        break
    else:
        print("Invalid username or password. Please try again.")