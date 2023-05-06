"""Credit calculator which calculate with raw values from terminal"""
import math
import argparse


class LoanCalculator:
    """Calculate all type of payments in terminal"""
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--principal", type=int)
        parser.add_argument("--payment", type=int, required=False)
        parser.add_argument("--interest", type=float)
        parser.add_argument("--periods", type=int)
        parser.add_argument("--annuity", type=float)
        parser.add_argument("--type", type=str)
        self.args = parser.parse_args()

    @staticmethod
    def calculate_periods(payment, percents):
        """Calculate month for loan in terminal"""
        var = percents * 0.01 / 12
        coefficient = math.ceil(math.log(payment / (payment - var), 1 + var))
        years = coefficient // 12
        months = coefficient % 12
        if months == 0:
            print(f"It will take {years} years to repay this loan!\n")
        elif years == 0:
            print(f"It will take {months} months to repay this loan!\n")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!\n")
        print(f"Overpayment {int(payment * coefficient)}")

    @staticmethod
    def calculate_annuity(all_money, periods, percents):
        """Calculate annual payments in terminal"""
        var = percents * 0.01 / 12
        coefficient = all_money * var * pow(1 + var, periods) / (pow(1 + var, periods) - 1)
        print(f"Your monthly payment = {math.ceil(coefficient)}!\n")
        print(f"Overpayment {math.ceil(coefficient) * periods - all_money}")

    @staticmethod
    def calculate_principal(payment, periods, percents):
        """Calculate all money of loan in terminal"""
        print(payment)
        print(periods)
        print(percents)
        if percents is None:
            print("Incorrect parameters")
            return
        var = percents * 0.01 / 12
        coefficient = payment / (var * pow(1 + var, periods) / (pow(1 + var, periods) - 1))
        print(f"Your loan principal = {math.floor(coefficient)}!\n")
        print(f"Overpayment {math.ceil(payment * periods - coefficient)}")
        return

    @staticmethod
    def calculate_diff(all_money, periods, percent):
        """Calculate differential payments in terminal"""
        var = percent * 0.01 / 12
        result = 0
        for month in range(periods):
            coff = math.ceil(all_money / periods + var * (all_money - all_money * month / periods))
            result += coff
            print(f"Month {month + 1}: payment is {coff}")
        print(f"Overpayment {result - all_money}")

    def run(self):
        """Function to run program in console"""
        if self.args.type == "diff" and self.args.payment is not None:
            print("Incorrect parameters")
            return
        if self.args.interest is None or self.args.interest < 0:
            print("Incorrect parameters")
            return
        if self.args.type == "annuity":
            match self.args.payment, self.args.principal, self.args.periods:
                case (None, _, _):
                    self.calculate_annuity(self.args.principal, self.args.periods, self.args.interest)
                case (_, None, _):
                    self.calculate_principal(self.args.payment, self.args.periods, self.args.interest)
                case (_, _, None):
                    self.calculate_periods(self.args.payment, self.args.interest)
                case _:
                    print("Incorrect parameters")
                    return
        elif self.args.type == "diff":
            if self.args.principal is not None and self.args.periods is not None:
                self.calculate_diff(self.args.principal, self.args.periods, self.args.interest)
            else:
                print("Incorrect parameters")
                return


if __name__ == "__main__":
    calculator = LoanCalculator()
    calculator.run()
