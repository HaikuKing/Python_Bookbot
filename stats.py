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