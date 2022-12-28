"""Coffee machine with classes project"""


class CoffeeMachine:
    """Coffee machine body"""
    def __init__(self):
        self.money = 550
        self.water = 450
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9

    def remaining(self):
        """Function to show how much ingredients still remaining in machine"""
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money""")

    def buy(self):
        """Function which give to user a question about drink which that need"""
        print("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,
        4 - hot milk, 5 - water, back - to main menu:""")
        choice = input()
        if choice == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
        elif choice == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 15
                print("I have enough resources, making you a coffee!")
        elif choice == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 20
                print("I have enough resources, making you a coffee!")
        elif choice == "4":
            if self.milk < 350:
                print("Sorry, not enough milk!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.milk -= 350
                self.cups -= 1
                self.money += 10
                print("I have enough resources, making you a hot milk!")
        elif choice == "5":
            if self.water < 300:
                print("Sorry, not enough water!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 300
                self.cups -= 1
                self.money += 5
                print("I have enough resources, making you a cup of water!")
        elif choice == "back":
            return print("Ok, let's go to main menu")

    def fill(self):
        """Function to add some ingredients into machine"""
        print("Write how many ml of water do you want to add:")
        added_water = int(input())
        self.water += added_water
        print("Write how many ml of milk do you want to add:")
        added_milk = int(input())
        self.milk += added_milk
        print("Write how many grams of coffee beans do you want to add:")
        added_coffee_beans = int(input())
        self.coffee_beans += added_coffee_beans
        print("Write how many disposable cups of coffee do you want to add:")
        added_cups = int(input())
        self.cups += added_cups

    def take(self):
        """Function to take money from machine"""
        print(f"I gave you {self.money}")
        self.money = 0


coffee_machine = CoffeeMachine()


def main_part():
    """Part to start a coffee machine's work"""
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            coffee_machine.buy()
        elif action == "fill":
            coffee_machine.fill()
        elif action == "take":
            coffee_machine.take()
        elif action == "remaining":
            coffee_machine.remaining()
        elif action == "exit":
            break
        else:
            print("Invalid action")
    return print("That's all, goodbye!")


main_part()
