import string
import os
import time


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("""
        ██████╗  █████╗ ███████╗███████╗
        ██╔══██╗██╔══██╗██╔════╝██╔════╝
        ██████╔╝███████║███████╗███████╗
        ██╔═══╝ ██╔══██║╚════██║╚════██║
        ██║     ██║  ██║███████║███████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
        PASSWORD  STRENGTH  ANALYZER

          
        Language: Python 3.x  
        Note: Passwords won't be logged anywhere.
          
    --------------------------------------------------------------
    """)
    try:
        user_input = input("Enter your password (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
    except TypeError:
        print("Invalid input. Please enter a valid string.")
        continue
    
    point = 0
    count_total = 0
    count_letters = 0
    count_numbers = 0
    count_special = 0

    for i in user_input:
        count_total += 1
        if i in string.ascii_letters:
            count_letters += 1
        elif i in string.digits:
            count_numbers += 1
        else:
            count_special += 1

        if i in string.ascii_uppercase:
            point += 3

    if  6 > count_total > 0:
        print("Input is too short. Minimum length is 6 characters.")

    else:
        print("Analyzing...")
        time.sleep(1.4)

        if 6 <= count_total < 10:
            point += 2
        elif 10 <= count_total:
            point += 5
        
        if  3 > count_numbers > 0:
            point += 2
        elif 3 <= count_numbers < 8:
            point += 4
        elif 8 <= count_numbers:
            point += 6
        
        if 3 >= count_special > 0:
            point += 3
        elif 3 <= count_special < 6:
            point += 6
        elif 6 <= count_special:
            point += 9

    if point < 6:
        strength = "Weak"
    elif 6 <= point < 10:
        strength = "Normal"
    elif 10 <= point < 15:
        strength = "Strong"
    elif 15 <= point:
        strength = "Insane"
    
    print(f"Strength: {strength}")

    c = input("Do you want to analyze another input? (y/n): ")
    if c.lower() != 'y':
        print("Exiting the program.")
        break
    