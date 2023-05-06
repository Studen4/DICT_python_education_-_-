"""
Calculator to solve credit questions
"""
from math import log


class LoanCalculator:
    """Class to functions which works as calculator for loans, percents, annual etc."""
    def __init__(self):
        pass

    @staticmethod
    def month_to_pay(start_money_sum: int, monthly_payment: int):
        """Function to calculate how much month you need to pay credit"""
        months = start_money_sum // monthly_payment
        if start_money_sum % monthly_payment > 0:
            months += 1
        return months

    @staticmethod
    def payment_for_month(start_money_sum: int, months: int):
        """Function to calculate how much you need to pay for each other month"""
        payment = start_money_sum // months
        last_payment = start_money_sum - (months - 1) * payment
        if last_payment == payment:
            return payment,
        else:
            return payment, last_payment

    @staticmethod
    def annual_payment(start_money_sum: int, year_percent: float, years: int):
        """Function to calculate annual payment"""
        some_var = year_percent / 100
        first_coefficient = some_var * (1 + some_var) ** years
        second_coefficient = (1 + some_var) ** years - 1
        annual_payment = start_money_sum * (first_coefficient / second_coefficient)
        return annual_payment

    @staticmethod
    def period_to_repay(start_money_sum: int, payment: float, modification: float):
        """Function to calculate which period you have to repay the loan"""
        some_var = modification / 1200
        periods = -(-log(payment / (payment - some_var * start_money_sum)) // log(1 + some_var))
        years = periods // 12
        months = periods % 12
        if years == 0:
            return f"It will take {months} months to repay this loan!"
        elif months == 0:
            return f"It will take {years} years to repay this loan!"
        else:
            return f"It will take {int(years)} years and {int(months)} months to repay this loan!"

    @staticmethod
    def loan_principal(annuity_payment: float, periods: int, loan_percents: float):
        """Function to calculate some kind of loan principal"""
        i = loan_percents / 1200
        first_coefficient = i * (1 + i) ** periods
        second_coefficient = (1 + i) ** periods - 1
        loan_principal = annuity_payment / (first_coefficient / second_coefficient)
        return int(round(loan_principal))

    @staticmethod
    def differentiated_payment(money_sum: float, payments: float, mod: float, month: int):
        """Function to calculate overpayment of credit"""
        money = money_sum / payments
        percent = mod / 1200
        return money + percent * (money_sum - (money * (month - 1)))


def months_to_years_and_months(months: int):
    """Some important function to change raw month to years + month format"""
    years = months // 12
    remaining_months = months % 12
    match (years, remaining_months):
        case (0, 1):
            return f"{remaining_months} month"
        case (1, 0):
            return f"{years} year"
        case (1, 1):
            return f"{years} year and {remaining_months} month"
        case (1, _):
            return f"{years} year and {remaining_months} months"
        case (_, 0):
            return f"{years} years"
        case (_, 1):
            return f"{years} years and {remaining_months} month"
        case (_, _):
            return f"{years} years and {remaining_months} months"


def starter():
    """Main program function, which starts it"""
    calculator = LoanCalculator()
    all_money = int(input("Enter the money sum which you want to calculate:"))
    print("""
    What do you want to calculate?
    type "m" - for number of monthly payments,
    type "mp" - for the monthly payment:
    type "a" - for the annual yearly payment:
    type "n" - for number of monthly payments:
    type "p" - for loan principal calculations:
    type "d" - for differentiated payment
                             """)
    type_of_calculations = input(">")
    match type_of_calculations:
        case "m":
            monthly_payment = int(input("Enter the monthly payment:"))
            months = calculator.month_to_pay(all_money, monthly_payment)
            return f"It will take {months_to_years_and_months(months)} to repay the loan"
        case "mp":
            months = int(input("Enter the number of months:"))
            payment, last_payment = calculator.payment_for_month(all_money, months)
            if last_payment:
                return f"Your monthly payment = {payment} and the last payment = {last_payment}."
            else:
                return f"Your monthly payment = {payment}."
        case "a":
            year_percent = float(input("Enter the annual interest modification:"))
            years = int(input("Enter the number of years:"))
            annual_payment = calculator.annual_payment(all_money, year_percent, years)
            print(f"Your annual payment = {round(annual_payment, 2)}.")
            months = years * 12
            return f"It will take {months_to_years_and_months(months)} to repay the loan"
        case "n":
            payment = float(input("Enter the monthly payment:"))
            modification = float(input("Enter the loan percent:"))
            result = calculator.period_to_repay(all_money, payment, modification)
            return result
        case "p":
            annuity_payment = float(input("Enter the annuity payment:"))
            periods = int(input("Enter the number of periods:"))
            loan_percent = float(input("Enter the loan percent:"))
            loan_principal = calculator.loan_principal(annuity_payment, periods, loan_percent)
            return f"Your loan principal = {loan_principal}!"
        case "d":
            total_paid = 0
            money_sum = all_money
            payments = int(input("Enter the number of periods:"))
            mod = float(input("Please, enter loan percent:"))
            for payment_month in range(1, payments + 1):
                payment = calculator.differentiated_payment(money_sum, payments, mod, payment_month)
                total_paid += payment
                print(f"Month {payment_month}: payment is {round(payment, 2)}")
            overpayment = total_paid - money_sum
            return f"Overpayment = {round(overpayment, 2)}"
        case _:
            return "Unknown operation"


print(starter())
