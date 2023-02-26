"""Some module to start test"""

from tests import Tests


def starter():
    """Main function to start program"""
    counter_of_tests = 0
    counter_of_right = 0
    result = "No results ^_^"
    print("""
    Arithmetic test 1.0
    -------------------------------------------
    In this math test you receive 5 questions
    If you answer for question is right - your score grow up!
    Good luck!

    So, pick difficulty of tests:
    >ez - Easy
    >mid - Middle 
    >imp - Calculator 
    (input without >)
    """)

    test_pick = input(">")
    if test_pick == "ez":
        while counter_of_tests <= 5:
            test = Tests()
            test.easy_test()
            user_answer = input('> ')
            answer = test.check_answer(user_answer)
            print(answer)
            if answer == "Right!":
                counter_of_right += 1
            counter_of_tests += 1
            if counter_of_right <= 3:
                result = "Bruh, it's so bad man!"
            elif counter_of_right == 4:
                result = "Nice work, but you can do it better!"
            elif counter_of_right == 5:
                result = "Perfect work! You really good in math!"
        print(f'{result} Your score - {counter_of_right}/5')
        total_points = counter_of_right * 1
        point_calculate(total_points)
    elif test_pick == "mid":
        while counter_of_tests <= 5:
            test = Tests()
            test.mid_test()
            user_answer = input('> ')
            answer = test.check_answer(user_answer)
            print(answer)
            if answer == "Right!":
                counter_of_right += 1
            counter_of_tests += 1
            if counter_of_right <= 3:
                result = "Bruh, it's so bad man!"
            elif counter_of_right == 4:
                result = "Nice work, but you can do it better!"
            elif counter_of_right == 5:
                result = "Perfect work! You really good in math!"
        print(f'{result} Your score - {counter_of_right}/5')
        total_points = counter_of_right * 5
        point_calculate(total_points)
        return total_points
    elif test_pick == "imp":
        while counter_of_tests <= 5:
            test = Tests()
            test.insane_test()
            user_answer = input('> ')
            answer = test.check_answer(user_answer)
            print(answer)
            if answer == "Right!":
                counter_of_right += 1
            counter_of_tests += 1
            if counter_of_right <= 3:
                result = "Bruh, it's so bad man!"
            elif counter_of_right == 4:
                result = "Nice work, but you can do it better!"
            elif counter_of_right == 5:
                result = "Perfect work! You really good in math!"
        print(f'{result} Your score - {counter_of_right}/5')
        total_points = counter_of_right * 20
        point_calculate(total_points)


def point_calculate(points):
    """Some function to append scores with name of player in results.txt"""
    if points > 0:
        print(f"You've earned {points} points!")
        save_results = input("Do you want to save the result? (Yes/No)").lower()
        if save_results == "yes":
            name = input("Enter your name:")
            with open("results.txt", "a") as file:
                file.write(f"{name}\nScore: {points}\n")
                print("Results saved successfully!")
                exit()
        else:
            exit()


print(starter())
