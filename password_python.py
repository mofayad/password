attempts = 0
correct_password = "DEV@2023"
secret_answer = "Favorite color"
while attempts <= 3:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Hello")
        break
    else:
        attempts += 1
        if attempts == 3:
            secret_response = input(f"What is your {secret_answer.lower()}? ")
            if secret_response == secret_answer:
                print("Hello")
                break
            else:
                print("Access denied")
                break
if attempts > 3:
    secret_response = input(f"What is your {secret_answer.lower()}? ")
    if secret_response == secret_answer:
        print("Hello")
        print("Access denied")