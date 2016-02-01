# Code from http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python

_end = "_end_"


def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root


def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict:
            return True
        else:
            return False

if __name__ == "__main__":
    trie = make_trie("foo", "bar", "baz", "barz")
    print in_trie(trie, "bar")
