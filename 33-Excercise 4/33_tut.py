import random
import string

def add_random_alpha(word):  
    random_words_small = string.ascii_lowercase
    random_words_large = string.ascii_uppercase
    random_three_alpha_start = ''.join(random.sample(random_words_large, 3))
    random_three_alpha_end = ''.join(random.sample(random_words_small, 3))
    new_str = random_three_alpha_start + word[1:3] + word[0] + random_three_alpha_end
    return new_str

str_input = input("Enter the Message: ")
words = str_input.split()

encoded_words = []
reversed_words = []
flag = input("Enter 1 for Encoding: ")

if flag == "1":
    for word in words:
        if len(word) >= 3:
            encoded_message = add_random_alpha(word)
            encoded_words.append(encoded_message)
        else:
            encoded_words.append(word)

    encoded_message = ' '.join(encoded_words)
    print("Encoded message:", encoded_message)

else:
    for word in words:
        if len(word) == 2:
            reversed_words.append(word[::-1])
        else:
            reversed_words.append(word)

    reversed_message = ' '.join(reversed_words)
    print("Reversed message:", reversed_message)
