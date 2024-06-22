import hashlib

print("Welcome to the Simple Password Manager!")
#Create an empty dictionary to store the usernames/passwords
passwords = {}

def hash_password(password):
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

#Asking the user to save usernames/passwords using the program
while True:
    website = input("Enter the website or application name: ")
    password = input("Enter the password for {}: ".format(website))
    hashed_password = hash_password(password)
    passwords[website] = hashed_password
    print("Password saved successfully.")

    another = input("Do you want to add another password? (yes/no): ")
    if another.lower() != 'yes': #.lower converts into lowercase
        break

#Ask the user to check if what they have entered is the password they have saved
while True:
    website_to_check = input("Enter the website or application name to check its password: ")
    if website_to_check in passwords:
        entered_password = input("Enter your password for {}: ".format(website_to_check))
        hashed_entered_password = hash_password(entered_password)
        if hashed_entered_password == passwords[website_to_check]:
            print("Password correct!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("No password found for {}. Please add it to the password manager.".format(website_to_check))

    another_check = input("Do you want to check another password? (yes/no): ")
    if another_check.lower() != 'yes':
        print("Exiting password manager. Goodbye!")
        break
