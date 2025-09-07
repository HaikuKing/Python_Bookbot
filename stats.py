def get_word_count(text):

    num_word = 0
    for word in text:
        num_word += 1
    return num_word

def get_character_count(text):
    character_count = {}

    for word in text:
        for letter in word:
            if letter not in character_count:
                character_count[letter] = 1
            else:
                character_count[letter] += 1

    return character_count

def list_key(dict_list):
    return dict_list["num"]

def sorted(dict):
    char_list = []

    for char in dict:
        num = dict[char]
        if char.isalpha() == True:
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=list_key)

    return char_list