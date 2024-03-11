def user_choice():
    # Variables

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_range = False

    # Two conditions to check
    # Digit or within _range == False
    while not choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        # Digit check
        if not choice.isdigit():
            print("Sorry that is not a digit!")

        # Range check
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("You are out of acceptable range (0-10)")
                within_range = False

    return int(choice)


user_choice()
