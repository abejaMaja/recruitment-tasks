# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
# NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE


def missing_numbers(list, n):
    """ generates a list of missing numbers between given list and range of numbers.

    Args:
        list (list): unsorted list of numbers.
        n (int): range of numbers.

    Returns:
        list: missing numbers between given list and range of numbers.
    """

    list_result = []
    for elem in range(1, n+1):
        if elem not in list:
            list_result.append(elem)

    return list_result
