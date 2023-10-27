# TODO: change the find function so that it looks through `text` more
# systematically, that it returns `-1` if `word` cannot be found.

from random import randrange

def find(word: str, text: str) -> int:
    """Find a word in a string."""
    word_len = len(word)
    index = -1
    found = False
    while index < len(text) and not found:
        index += 1
        if text[index:index+word_len] == word:
            found = True
    if found:
        return index
    else:
        return index - (len(text) + 1)


# from random import randrange

# def find(word: str, text: str) -> int:
#     """Find a word in a string."""
#     word_len = len(word)
#     text_len = len(text)
#     found = False
#     while not found:
#         i = randrange(text_len - word_len)
#         if text[i : i + word_len] == word:
#             found = True
#     return i