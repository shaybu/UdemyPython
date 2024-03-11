from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]


#
#
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


#
#
results = shuffle_list(example)
#
my_list = ['', 'o', '']
shuffle_list(my_list)


# print(my_list)

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0,1, or 2")

    return int(guess)


player_guess()

myindex = player_guess()


def check_guess(mylist, guess):
    if mylist[guess] == 'o':
        print("Correct")
    else:
        print("Wrong Guess!")
        print(mylist)


# INIT LIST
mylist = ['', 'o', '']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list, guess)


