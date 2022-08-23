import random


def main():
    data = get_data()
    print(data)
    words = validate_word(data)
    display_message(words)

def validate_word(data):
    words = []
    for word in data:
        if word[0] in 'aeiou' and word[1] not in 'aeiou' and word[2] not in 'aeiou':
                    words.append(word)
        elif word[0] not in 'aeiou' and word[1] in 'aeiou'and word[2] not in 'aeiou':
                words.append(word)
    return words

def display_message(words):
    print('-'.join(words))



def get_data():
    word = []
    for i in range(5):
        word.append(random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz'))
    return word

main()