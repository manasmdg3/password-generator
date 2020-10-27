import random, string, pyperclip, time

print('''
▒█▀▄▒▄▀▄░▄▀▀░▄▀▀░█░░▒█░▄▀▄▒█▀▄░█▀▄░░░▄▀▒▒██▀░█▄░█▒██▀▒█▀▄▒▄▀▄░▀█▀░▄▀▄▒█▀▄
░█▀▒░█▀█▒▄██▒▄██░▀▄▀▄▀░▀▄▀░█▀▄▒█▄▀▒░░▀▄█░█▄▄░█▒▀█░█▄▄░█▀▄░█▀█░▒█▒░▀▄▀░█▀▄
Strong Password Generator\t\t\t\tby Manas Dattagupta
Github: https://github.com/manasmdg3/password-generator/
''')

while True:
    try:
        passwordLength = int(input("Enter desired length of the password (Between 7 & 100): "))
        if passwordLength <7 or passwordLength >100:
            print("Invalid Length.")
            continue
        
        startTime = time.time()
        password = random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for x in range (passwordLength-1):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + "@!#.%&*_-")

        pyperclip.copy(password)
        endTime = time.time()
        print(".---------------------------------.\n| Password generated successfully |\n'---------------------------------'\n" + password + "\n\nPassword is copied to clipboard!")
        print("Time taken to generate : " + "{:.0f}".format((endTime - startTime)*1000) +" miliseconds")
        close = input("Press Enter to close . . .")
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
