"""Simple Tic-tac-toe game on Python"""

DICT_FOR_NET_BOXES = {
    "1,1": "━",
    "1,2": "━",
    "1,3": "━",
    "2,1": "━",
    "2,2": "━",
    "2,3": "━",
    "3,1": "━",
    "3,2": "━",
    "3,3": "━"
}
CHECKOUT_ENTERED_POS = []


# 1-st stage
# input_for_width = input("Enter width: >>>")
# input_for_height = input("Enter height: >>>")
#
#
# def net_shower(height, width):
#     width_string = "X "*int(width)
#     for checkout in range(0, int(height)):
#         print(width_string)
#     return ""
#
#
# print(net_shower(input_for_height, input_for_width))
# 2-nd stage
# input_net_mode = input("Enter cells:")
#
#
# def net_creator(mode):
#     return (f'''
# ---------
# |{mode[0:3]}|
# |{mode[3:6]}|
# |{mode[6:9]}|
# ---------
#     ''')
#
#
# print(net_creator(input_net_mode))
# 3-rd stage
# check_net_mod = input("Enter cells:")
#
#
# def net_mode_checker(mode):
#     upd_mode = list(mode)
#     print(upd_mode)
#     print(f'''
# ---------
# |{mode[0:3]}|
# |{mode[3:6]}|
# |{mode[6:9]}|
# ---------
#     ''')
#     if upd_mode[0] == upd_mode[1] == upd_mode[2]:
#         print(f'{upd_mode[0]} wins!')
#     elif upd_mode[3] == upd_mode[4] == upd_mode[5]:
#         print(f'{upd_mode[3]} wins!')
#     elif upd_mode[6] == upd_mode[7] == upd_mode[8]:
#         print(f'{upd_mode[6]} wins!')
#     elif upd_mode[0] == upd_mode[3] == upd_mode[6]:
#         print(f'{upd_mode[0]} wins!')
#     elif upd_mode[1] == upd_mode[4] == upd_mode[7]:
#         print(f'{upd_mode[1]} wins!')
#     elif upd_mode[2] == upd_mode[5] == upd_mode[8]:
#         print(f'{upd_mode[2]} wins!')
#     elif upd_mode[0] == upd_mode[4] == upd_mode[8]:
#         print(f'{upd_mode[0]} wins!')
#     elif upd_mode[2] == upd_mode[4] == upd_mode[6]:
#         print(f'{upd_mode[2]} wins!')
#     elif placement_checker(check_net_mod) == "Impossible":
#         print("Impossible!")
#     elif "_" in upd_mode:
#         print(f'Game not finished!')
#     else:
#         print(f'Draw')
#     return ""
#
#
# def placement_checker(placement):
#     upd_placement = list(placement)
#     result_for_x = upd_placement.count("X")
#     result_for_o = upd_placement.count("0")
#     result_checker = result_for_x - result_for_o
#     if result_checker < -1:
#         return f'Impossible'
#     elif result_checker > 1:
#         return f'Impossible'
#     else:
#         return ""
#
#
# net_mode_checker(check_net_mod)
# 4-5 stages

def manual():
    """Function to show how to play this game"""
    print("""
    Welcome to simple tic-tac-toe game!!!
    This game about two players which enter box numbers
    and wants to get 3 boxes with their symbols in row.
    ---------------------------------------------------
    The format of the entered data should be as follows:
    (1, 1) (1, 2) (1, 3)
    (2, 1) (2, 2) (2, 3)
    (3, 1) (3, 2) (3, 3)
    ---------------------------------------------------
    You must enter the values according to the given format,
    so that the game works correctly and there are no errors.
    Example of input: 1,2
    not -> one,two
    not -> 1,4
    not -> Something else...
    """)
    return ""


def net_visualisation(needed_dict):
    """Function to show net status"""
    print(f'''
-------
|{needed_dict["1,1"]} {needed_dict["1,2"]} {needed_dict["1,3"]}|
|{needed_dict["2,1"]} {needed_dict["2,2"]} {needed_dict["2,3"]}|
|{needed_dict["3,1"]} {needed_dict["3,2"]} {needed_dict["3,3"]}|
-------
''')
    return ""


def players_turns(dict_for_check, num):
    """Checker: which player must pick box now"""
    if num == 1:
        print(f"It's player {num} turn!")
        while True:
            player_first_turn = input("Enter the coordinates:")
            if correct_checker(player_first_turn, CHECKOUT_ENTERED_POS) == "Input is correct!":
                dict_for_check[player_first_turn] = "X"
                break
            correct_checker(player_first_turn, CHECKOUT_ENTERED_POS)
    elif num == 2:
        print(f"It's player {num} turn!")
        while True:
            player_second_turn = input("Enter the coordinates:")
            if correct_checker(player_second_turn, CHECKOUT_ENTERED_POS) == "Input is correct!":
                dict_for_check[player_second_turn] = "0"
                break
            correct_checker(player_second_turn, CHECKOUT_ENTERED_POS)
    return ""


def correct_checker(some_input, checkout_list):
    """Checker: input correction"""
    some_input_upd = list(some_input)
    if some_input_upd[0] not in ["1", "2", "3"]:
        return print("Coordinates should be from 1 to 3!")
    if some_input_upd[2] not in ["1", "2", "3"]:
        return print("Coordinates should be from 1 to 3!")
    if some_input in checkout_list:
        return print("This cell is occupied! Choose another one!")
    if some_input not in checkout_list:
        checkout_list.append(some_input)
        print(checkout_list)
    elif some_input_upd[0].isdigit() or some_input_upd[2].isdigit() is False:
        return print("You should enter numbers!")
    return "Input is correct!"


def conditions_checker(checkout_dict):
    """End-game function to check who is winner"""
    if checkout_dict["1,1"] == checkout_dict["1,2"] == checkout_dict["1,3"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    elif checkout_dict["2,1"] == checkout_dict["2,2"] == checkout_dict["2,3"] in ["X", "0"]:
        print(f'{checkout_dict["2,1"]} - player win!')
    elif checkout_dict["3,1"] == checkout_dict["3,2"] == checkout_dict["3,3"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    elif checkout_dict["1,1"] == checkout_dict["2,1"] == checkout_dict["3,1"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    elif checkout_dict["1,2"] == checkout_dict["2,2"] == checkout_dict["3,2"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    elif checkout_dict["1,3"] == checkout_dict["2,3"] == checkout_dict["3,3"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    elif checkout_dict["1,1"] == checkout_dict["2,2"] == checkout_dict["3,3"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    elif checkout_dict["1,3"] == checkout_dict["2,2"] == checkout_dict["3,1"] in ["X", "0"]:
        print(f'{checkout_dict["1,1"]} - player win!')
    return ""


def main_game(dict_for_work):
    """Main game part function"""
    counter = 1
    manual()
    while True:
        net_visualisation(dict_for_work)
        if conditions_checker(dict_for_work) != "":
            exit()
        players_turns(dict_for_work, counter)
        if counter == 1:
            counter = counter + 1
        elif counter == 2:
            counter = counter - 1


main_game(DICT_FOR_NET_BOXES)
