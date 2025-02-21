def is_palindrome(s: str) -> bool:
    """
    Determines whether a given string is a palindrome

    Args:
        s: str: str, dubbed s

    Returns:
        bool: true or false, delineating whether the given input is a palindrome
        once capitalization, spaces, and alpha numeric numbers are ignored
    """
    s = s.lower()
    forward = []
    for letter in s:
        if letter.isalnum():
            forward.append(letter)
    #print(forward)

    backward = []
    for letter in s[::-1]:
        if letter.isalnum():
            backward.append(letter)
    #print(backward)

    # forward = ''.join(letter for letter in s if letter.isalnum())
    # backward = ''.join(letter for letter in s[::-1] if letter.isalnum())
    return forward == backward


def main():
    s = input("enter possible palindrome: ")
    answer = is_palindrome(s)
    print(answer)


if __name__ == '__main__':
    main()