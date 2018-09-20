# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5,
# DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


def decimal_list(start=20, stop=60, jump=5):
    """ generates a list of decimal numbers from 2.0 to 5.5"""

    return [x/10 for x in range(start, stop, jump)]
