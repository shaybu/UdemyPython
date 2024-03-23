def ask_for_int():
    while True:
        try:
            results = int(input("Please Provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break


ask_for_int()
