"""Class to work with robux exchanger"""
import json


class RobuxExchange:
    """Very important class to work with robux and exchange it"""
    def __init__(self):
        with open('list_of_currencies.json', encoding='utf-8') as file:
            self.exchange_rates = json.load(file)

    @staticmethod
    def convert_currency(amount, exchange_rate):
        """Function to convert money and use rate for this"""
        return round(amount * exchange_rate, 2)

    @staticmethod
    def convert_to_robux(amount, exchange_rate):
        """Function which convert robux"""
        return round(amount / exchange_rate, 2)

    @staticmethod
    def manual_part(user_pick):
        """Function to show inform messages"""
        match user_pick:
            case 1:
                print("""
        Choose one of the following options:
        1. Convert robux to other currency
        2. Convert other currency to robux
                    """)
            case 2:
                print("""
        Pick one of these formats of national currencies:
        USD - Dollar
        EUR - Euro
        UAH - Hryvnia
        BYN - Ruble
        PLN - Zloty
        HUF - Forint
        ZWD - Zimbabwe Dollar
                    """)
            case 3:
                return False

    def convert_robux_to_currency(self, robux_amount, currency):
        """Function to convert robux into some value"""
        if currency in self.exchange_rates:
            rate = self.exchange_rates[currency]
            converted_amount = self.convert_currency(robux_amount, rate)
            print(f"The total amount of {currency}: {converted_amount}")
        else:
            print("Invalid currency code.")

    def convert_currency_to_robux(self, currency, amount):
        """Function to convert some value to robux"""
        if currency in self.exchange_rates:
            rate = self.exchange_rates[currency]
            converted_amount = self.convert_to_robux(amount, rate)
            print(f"The total amount of robux: {converted_amount}")
        else:
            print("Invalid currency code.")

    def process_user_choice(self, option):
        """Function which choose type of converting"""
        match option:
            case "1":
                robux_amount = float(input("Please enter the number of robux you have: "))
                currency = input("Please enter the currency code (e.g., USD, EUR, UAH): ")
                self.convert_robux_to_currency(robux_amount, currency)
            case "2":
                currency = input("Please enter the currency code (e.g., USD, EUR, UAH): ")
                amount = float(input(f"Please enter the amount of {currency}: "))
                self.convert_currency_to_robux(currency, amount)
            case _:
                print("Invalid option. Please choose 1 or 2.")

    def main(self):
        """Main part function to start exchanger"""
        start_match = input("""
        Please, enter !start to run exchanger,
        or !help to get list of values with it names,
        enter !exit to leave program
        \n
        """)
        match start_match:
            case "!start":
                self.manual_part(1)
                option = input("Enter your choice (1 or 2): ")
                self.process_user_choice(option)
            case "!help":
                self.manual_part(2)
            case "!exit":
                self.manual_part(3)
