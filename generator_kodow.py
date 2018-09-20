# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH

def get_postcodes(x, y):
    """ return postal codes between two given arguments.

    Args:
        x (str): The first given postal code.
        y (str): The second given postal code.

    Returns:
        list: postal codes between two givenself.
    """

    x = int(x.replace('-',''))
    y = int(y.replace('-',''))

    list = []
    for n in range(x, y):
        begin = n // 1000
        end = n % 1000
        list.append('{:02}-{:03}'.format(begin, end))
    return list
