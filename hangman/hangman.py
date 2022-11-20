"""Simple hangman game project"""

# 1-st stage
print("HANGMAN")
# 2-nd stage
# Place for variables
list_of_words = ['python', 'java', 'javascript', 'php', "example",
                 "another", "good", "random", "word", "keygen"]
word_pitch = []
list_for_random = ["Something"]
list_for_checkout = []
COUNT_TO_WIN = 0
DEATH_COUNT = 0


# def simple_guesser(receive_word):
#     """For check that person survived or not"""
#     if receive_word == receiver:
#         result = "You survived!"
#     else:
#         result = "You lost!"
#     return result


# 3-rd stage

def randomizer(some_list):
    """For random choice word in list"""
    picker = id(some_list)
    random = str(picker)
    random_num = random[14]
    temporary_word = list_of_words[int(random_num)]
    return temporary_word


# 4-th stage
# guesser = input("Guess the word or input letter" + upd_receiver + ">")
# print(simple_guesser(guesser))
# 5-th stage
receiver = randomizer(list_for_random)
empty_list = list(("_" * len(receiver)))
# 6-7 stage


def appender():
    """Function to create pull of ___ on first start"""
    while True:
        while "".join(word_pitch) != ("_" * len(receiver)):
            word_pitch.append("_")
        return "".join(word_pitch)


def letter_checker(list_to_check, num):
    """Function to check letters and show itself result"""
    global COUNT_TO_WIN
    receiver_to_list = list(receiver)
    for i, x_changer in enumerate(list_to_check):
        if x_changer == num:
            z_changer = i
            for q_changer in range(len(receiver)):
                if q_changer == z_changer:
                    empty_list[q_changer] = receiver_to_list[q_changer]
                    COUNT_TO_WIN = COUNT_TO_WIN + 1
                    print("".join(empty_list))


def checker(new_guesser):
    """Function to check correction of input"""
    global DEATH_COUNT
    receiver_to_list = list(receiver)
    while empty_list != receiver_to_list:
        if len(new_guesser) != 1:
            print("You should input a single letter.")
            break
        elif new_guesser != new_guesser.lower():
            print("Please enter a lowercase English letter.")
            break
        elif new_guesser in list_for_checkout:
            print("You've already guessed this letter.")
            break
        elif new_guesser not in list_for_checkout:
            while True:
                try:
                    receiver_to_list.index(new_guesser)
                except ValueError:
                    print("That letter doesn't appear in the word")
                    DEATH_COUNT = DEATH_COUNT + 1
                letter_checker(receiver_to_list, new_guesser)
                list_for_checkout.append(new_guesser)
                break
            break


def main_game():
    """Main-game function which starts game processes"""
    starter = input("Type 'play' to play the game, 'exit' to quit:")
    if starter == "play":
        print(appender())
        while True:
            win_count = len(receiver)
            if COUNT_TO_WIN == win_count:
                print(f'{"You guessed the word "}{receiver}\n{"You survived!"}')
                print("Do you want to play again? [Yes / No]")
                receive_answer = input(">>>")
                revers(receive_answer)
                break
            elif DEATH_COUNT == 8:
                print("You lost!")
                print("Do you want to play again? [Yes / No]")
                receive_answer = input(">>>")
                revers(receive_answer)
                break
            new_guesser = input("Input a letter: >")
            checker(new_guesser)
    elif starter == "exit":
        print("Exiting ...")
        exit()
    else:
        main_game()


#  8-th stage
def revers(answer):
    """Function to replay the game"""
    if answer == "Yes":
        global COUNT_TO_WIN, DEATH_COUNT, receiver, empty_list
        COUNT_TO_WIN = 0
        DEATH_COUNT = 0
        receiver = randomizer(list_for_checkout)
        empty_list = list(("_" * len(receiver)))
        list_for_checkout.clear()
        word_pitch.clear()
        main_game()
    elif answer == "No":
        exit()
    else:
        print("Enter correctly")


main_game()
