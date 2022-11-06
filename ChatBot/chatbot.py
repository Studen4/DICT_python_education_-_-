"""Simple chatbot which can calculate your age and test you"""
#  1-st
bot_name = "Victor"
year = 2022
print("Hello! My name is", bot_name + ".")
print("I was created in", str(year) + ".")
#  2-st
print("Please, remind me your name.")
user_first_enter = input(">")
print("What a great name you have,", user_first_enter + "!")
#  3-st
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
first_remainder = input(">")
second_remainder = input(">")
third_remainder = input(">")


def age_guesser(f_number, s_number, t_number):
    """Function for age calculation"""
    updator = int(f_number)
    s_updator = int(s_number)
    t_updator = int(t_number)
    age = (updator * 70 + s_updator * 21 + t_updator * 15) % 105
    some_text = " that's a good time to start programming!"
    final_age = f'{"Your age is"} {age};{some_text}'
    return final_age


result = age_guesser(first_remainder, second_remainder, third_remainder)
print(result)
#  4-th
print("Now I will prove to you that I can count to any number you want.")
num_user_enter = input(">")
stop = (int(num_user_enter) + 1)
for num_user_enter in range(0, stop):
    print(num_user_enter, "!")
print("Completed, have a nice day!")
#  5-th
print("Let's test your programming knowledge.")
print("What programming environment are we in now?")
print("""1.Python
2.Pethon
3.Java
4.C#""")
test_answer = input("Pick your answer:")
while int(test_answer) != 1:
    print("Please, try again.")
    print("1.Python")
    print("2.Pethon")
    print("3.Java")
    print("4.C#")
    test_answer = input("Enter new answer:")
print("Congratulations, have a nice day!")
