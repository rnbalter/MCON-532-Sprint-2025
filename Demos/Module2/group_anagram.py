def group_anagrams(words: list[str]) -> dict[str, list[str]]:
    """
    Groups anagrams from the given list of words.

    Args:
        words (list[str]): List of input words.

    Returns:
        dict[str, list[str]]: Dictionary grouping words by their anagram signature.
    """
    anagrams = {} #dictionary ie a hash map

    for word in words:
        # Sort the word's characters to create a signature for anagrams
        key = ''.join(sorted(word)) #word in alphabetical order. join casts array  - join the str ie become str
        anagrams.setdefault(key, []).append(word)
        #key is str (ie of sorted chars)
        #anagrams = put in anagram if nothin assoc with key (ie if not there. key = this list string of characters) then initalize value to be a list.
        #if key already exists in the dictionary then appends word to anagrams list
        #key must be immutable thrf can be a str or tuple(can be diff types) = immuatable once created

    return anagrams


def main():
    words = ['listen', 'silent', 'enlist', 'hello', 'world', 'cat', 'act']
    result = group_anagrams(words)

    for key, anagrams in result.items():
        print(f'{key}: {anagrams}')


if __name__ == '__main__':
    main()
