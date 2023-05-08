"""Class to calculate currencies exchange from site"""
import requests


class CurrencyExchange:
    """Class to work with json files from site"""
    def __init__(self):
        self.api = 'http://www.floatrates.com/daily/{0}.json'
        self.cache = {}

    def cache_init(self, available_value: str, should_done_value: str):
        """Function to create cache in dict"""
        current_value = self.cache.get(available_value, {})
        if current_value.get(should_done_value) is None:
            value = self.get_value(available_value, should_done_value)
            current_value[should_done_value] = {"rate": value}
            self.cache[available_value] = current_value
        return self.cache[available_value][should_done_value]["rate"]

    def cache_value(self):
        """Function to return final cache version"""
        return self.cache_init

    def get_value(self, available_value: str, should_done_value: str) -> float:
        """Function to get values from site"""
        response = requests.get(self.api.format(available_value), timeout=5)
        data = response.json()
        exchange_rate = data[should_done_value]['rate']
        return exchange_rate

    def value_finder(self, available_value: str):
        """Function to calculate exchange"""
        should_done_value = input("Enter target currency: ").lower()
        exchange_rate = self.get_value(available_value, should_done_value)
        if exchange_rate == -1:
            print("Sorry, but your target currency is not found")
            return
        user_money = input(f"Enter amount of your money ({available_value}): ")
        target_money = float(user_money) * exchange_rate
        print(f"You will get {target_money} {should_done_value}")

    def main(self):
        """Function to start program work"""
        print("Welcome to the basic currency exchange!")
        value = input("Enter your currency: ").lower()
        try:
            self.value_finder(value)
        except ValueError as error:
            print(error)
