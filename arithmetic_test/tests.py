"""All kind of tests"""
import random


class Tests:
    """Class for work with math tests and create random of it"""
    def __init__(self):
        self.result = 0
        self.first_easy_value = random.randint(2, 9)
        self.second_easy_value = random.randint(2, 9)
        self.third_easy_value = random.randint(2, 9)
        self.first_mid_value = random.randint(1, 100)
        self.second_mid_value = random.randint(1, 100)
        self.third_mid_value = random.randint(1, 100)
        self.first_insane_value = random.randint(1, 1000)
        self.second_insane_value = random.randint(1, 1000)
        self.third_insane_value = random.randint(1, 1000)
        self.fourth_insane_value = random.randint(1, 1000)
        self.fifth_insane_value = random.randint(1, 1000)
        self.pool_2 = random.choice(['+', '-', '*', '/'])
        self.pool_1 = random.choice(['+', '-', '*', '/'])
        self.pool_3 = random.choice(['+', '-', '*', '/'])
        self.pool_of_add_mid = [1, 2]
        self.pool_of_add_insane = [0, 1, 2, 3, 4]
        self.visual_1 = 0
        self.visual_2 = 0
        self.visual_3 = 0
        self.visual_4 = 0
        self.visual_5 = 0

    def easy_test(self):
        """Easy test for arithmetic quiz"""
        print("Hard level is - 1")
        to_calculate = [self.first_easy_value, self.pool_1, self.second_easy_value, self.pool_2,
                        self.third_easy_value]
        print("".join(map(str, to_calculate)))
        self.result = self.calculate(to_calculate)
        return self.result

    def mid_test(self):
        """Middle test for arithmetic quiz"""
        print("Hard level is - 5")
        if random.choices([True, False], weights=[0.25, 0.75], k=1)[0]:
            picker = random.choice(self.pool_of_add_mid)
            raw_value = self.first_mid_value
            self.visual_1 = f'{raw_value}**{picker}'
            raw_value **= picker
            self.first_mid_value = raw_value
        if random.choices([True, False], weights=[0.25, 0.75], k=1)[0]:
            picker = random.choice(self.pool_of_add_mid)
            raw_value = self.second_mid_value
            self.visual_1 = f'{raw_value}**{picker}'
            raw_value **= picker
            self.first_mid_value = raw_value
        if random.choices([True, False], weights=[0.25, 0.75], k=1)[0]:
            picker = random.choice(self.pool_of_add_mid)
            raw_value = self.third_mid_value
            self.visual_1 = f'{raw_value}**{picker}'
            raw_value **= picker
            self.first_mid_value = raw_value
        to_calculate = [self.first_mid_value, self.pool_1, self.second_mid_value, self.pool_2,
                        self.third_mid_value]
        if self.visual_1 == 0:
            self.visual_1 = self.first_mid_value
        if self.visual_2 == 0:
            self.visual_2 = self.second_mid_value
        if self.visual_3 == 0:
            self.visual_3 = self.third_mid_value
        to_visual = [self.visual_1, self.pool_1, self.visual_2, self.pool_2, self.visual_3]
        print("".join(map(str, to_visual)))
        self.result = self.calculate(to_calculate)
        return self.result

    def insane_test(self):
        """Impossible test for arithmetic quiz"""
        print("Hard level is - 20")
        if random.choices([True, False], weights=[0.5, 0.5], k=1)[0]:
            self.first_insane_value **= random.choice(self.pool_of_add_insane)
        if random.choices([True, False], weights=[0.5, 0.5], k=1)[0]:
            self.second_insane_value **= random.choice(self.pool_of_add_insane)
        if random.choices([True, False], weights=[0.5, 0.5], k=1)[0]:
            self.third_insane_value **= random.choice(self.pool_of_add_insane)
        if random.choices([True, False], weights=[0.5, 0.5], k=1)[0]:
            self.fourth_insane_value **= random.choice(self.pool_of_add_insane)
        if random.choices([True, False], weights=[0.5, 0.5], k=1)[0]:
            self.fifth_insane_value **= random.choice(self.pool_of_add_insane)
        to_calculate = [self.first_insane_value, self.pool_1, self.second_insane_value, self.pool_2,
                        self.third_insane_value, self.pool_3, self.fourth_insane_value, self.pool_1,
                        self.fifth_insane_value]
        print("".join(map(str, to_calculate)))
        self.result = self.calculate(to_calculate)
        return self.result

    def calculate(self, list_to_calculate):
        """Function to calculate answers from list"""
        i = 1
        while i < len(list_to_calculate):
            operator = list_to_calculate[i]
            operand = list_to_calculate[i + 1]
            if operator == '*':
                list_to_calculate[i - 1:i + 2] = [list_to_calculate[i - 1] * operand]
                i -= 2
            elif operator == '/':
                list_to_calculate[i - 1:i + 2] = [list_to_calculate[i - 1] / operand]
                i -= 2
            else:
                i += 2
        result = list_to_calculate[0]
        i = 1
        while i < len(list_to_calculate):
            operator = list_to_calculate[i]
            operand = list_to_calculate[i + 1]
            if operator == '+':
                result = result + operand
            elif operator == '-':
                result = result - operand
            i += 2
        self.result = result
        return self.result

    def check_answer(self, user_answer):
        """Function to check answer correctly"""
        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Incorrect format. Try again!")
            return False

        if user_answer == round(self.result):
            return "Right!"
        else:
            return "Wrong!"
            
