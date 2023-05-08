"""Module to work with all kinds of exchangers"""
from robux_exchange import RobuxExchange
from currencies_exchange import CurrencyExchange


def starter(variant_of_start):
    """Function to give user opportunity to choose exchanger"""
    if variant_of_start == "1":
        basic_exchanger = CurrencyExchange()
        basic_exchanger.main()
    elif variant_of_start == "2":
        robux_exchanger = RobuxExchange()
        robux_exchanger.main()


if __name__ == '__main__':
    print("""Please pick type of convertor:
1. Useless normal values exchange
2. MOST IMPORTANT THING IN LIFE - Robux currencies exchange
    """)
    while True:
        CONVERTOR_PICK = str(input(">>>"))
        starter(CONVERTOR_PICK)
