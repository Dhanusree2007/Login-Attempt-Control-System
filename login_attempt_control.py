import time
# Correct credentials
correct_username = "admin"
correct_password = "Secure123"
# Maximum attempts
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("\nLogin Successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("\nIncorrect username or password.")
        if remaining > 0:
            print(f"Remaining attempts: {remaining}")
        else:
            print("\nToo many failed attempts!")
            print("Access temporarily blocked for 10 seconds...")
            time.sleep(10)
            print("Please try again later.")