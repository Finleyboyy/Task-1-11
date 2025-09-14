# correct login info
correct_user = "python"
correct_pass = "rules"

tries = 0

# keep asking until correct or 5 tries
while tries < 5:
    user = input("Enter username: ")
    password = input("Enter password: ")

    if user == correct_user and password == correct_pass:
        print("Welcome")
        break
    elif user != correct_user and password != correct_pass:
        print("Both username and password are wrong")
    elif user != correct_user:
        print("Username is wrong")
    elif password != correct_pass:
        print("Password is wrong")

    tries = tries + 1

if tries == 5:
    print("Access denied")
