def separator(character: str = '-', length: int = 62) -> None:
    """
    Prints separator using character '-' as default character with default
    length of 62 characters.
    """
    print(character * length)


def safe_div(a, b):
    """
    Safe division operation. When b is equal to zero, this function returns 0.
    Otherwise it returns result of a divided by non-zero b.

    :param a: number a
    :param b: number b
    :return: a divided by b or zero
    """
    if b == 0:
        return 0
    return a / b
