"""Simple program to calculate money which spends on dinner party"""

import random

dictionary_of_unlucky = {}
list_of_received_words = receiver = []
var_for_append = list_of_received_words


# 1-st stage
# 2-nd stage
def first_input():
    """Function to calculate money spends by joined people for dinner"""
    num = int(input("Enter the number of friends joining (including you):"))
    lucky_num = num - 1
    if num == 0:
        return print("No one is joining for the party")
    checker = int(input("Enter the total amount:"))
    print("Enter the name of every friend (including you), each on a new line:")
    if num > 0:
        for i in range(0, num):
            inputer = str(input(">"))
            var_for_append.append(inputer)
            var_for_append.append(distributor(checker, lucky_num))
            i += 1
            dictionary_of_unlucky[inputer] = distributor(checker, num)
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        lucky_checker = input(">")
        if lucky_checker == "No":
            print("No one is going to be lucky")
            return print(dictionary_of_unlucky)
        if lucky_checker == "Yes":
            upd_dict_to_list = list(dictionary_of_unlucky)
            lucky_man = random.choice(upd_dict_to_list)
            print(f'{lucky_man} is the lucky one!')
            index_for_remove = var_for_append.index(lucky_man)
            num_which_removes = index_for_remove + 1
            list_of_received_words.pop(num_which_removes)
            list_of_received_words.pop(index_for_remove)
            dictionary_of_unlucky.clear()
            without_lucky_list = {receiver[i]: receiver[i + 1] for i in range(0, len(receiver), 2)}
            result = lucky_adder(without_lucky_list, lucky_man)
            return print(result)
    return print("Please enter correctly next time!")


# 3-4 stage
def distributor(first_digit, second_digit):
    """Simple function to calculate which money append every join person"""
    result = first_digit / second_digit
    return round(result, 2)


def lucky_adder(without_lucky_list, lucky_person):
    """Simple function to show lucky person in final dictionary"""
    without_lucky_list[lucky_person] = "0"
    return without_lucky_list


first_input()
