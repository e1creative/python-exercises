def print_upper_words(words):
    """Print each word in uppercase on a sep line.

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """

    for word in words:
        print(word.upper())


def print_upper_words_e(words):
    """Print each word in uppercase on a sep line, if the word starts with E or e.

        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words_any(words, must_start_with):
    """Print each word in uppercase on a sep line if starts with one of given list of letters

        >>> print_upper_words_any(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print_upper_words(["Programming", "is", "pretty", "fun"])
print_upper_words_e(["eagle", "Edward", "Alfred"])
print_upper_words_any(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])