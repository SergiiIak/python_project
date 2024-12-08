from eng_vowels.vowels import count_vowels

if __name__ == '__main__':
    input_str = input("Enter a string: ")
    print(f"the given string contains {count_vowels(input_str)} English vowels")