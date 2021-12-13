
def has_numbers(inputString):
    """check whether a given string has numbers in it or not

    Args:
        inputString (String): (years of experience) string, in our case

    Returns:
        Boolean: True: if any char of the string is a digit, False: otherwise
    """
    return any(char.isdigit() for char in inputString)
