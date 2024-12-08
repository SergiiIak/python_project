def count_vowels(input_string: str) -> int:
    """
    Counts the vowels of the English alphabet in a string of arbitrary length.
    :param input_string: a string of arbitrary length
    :return: number of vowels
    """

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
