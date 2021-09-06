import argparse
import random
import string

cipher_key = {}

def generate_key(seed, key):
    # Create dictionary with each letter of the alphabet to track which letters have been shuffled.
    # alphabet = {}
    # for letter in list(string.ascii_lowercase):
    #     alphabet[letter] = False

    # Track which letters have been used in the generated key
    alphabet = string.ascii_lowercase
    alphabet_length = len(alphabet)
    letter_is_used = [False] * len(alphabet)

    # # Seeding the random algorithm results allows the same key to be used for multiple messages, 
    # # as long as they use the same seed input.
    # random.seed(seed)
    # for letter in alphabet.keys: 
    #     shuffled = False
    #     while not shuffled:
    #         new_position = random.randint(0, 26)
    #         if not alphabet[new_position]:
    #             key[letter]

    print("generate key")
    random.seed(seed)
    for i in range(0, alphabet_length):
        shuffled = False
        while not shuffled:
            new_position = random.randint(0, alphabet_length-1)
            if not letter_is_used[new_position] and i is not new_position:
                key[alphabet[i]] = alphabet[new_position]
                letter_is_used[new_position] = True
                shuffled = True

    print("key done")
    print(key)


def main(): 
    print('Use puzzle_script to prepare messages for your RPG.  See --help for more information.')

    parser = argparse.ArgumentParser("Use puzzle_script to prepare messages for your RPG.\nThis program allows you to apply a substitution cipher and alternative fonts to your messages to add depth and character to your game.")
    parser.add_argument('--input', metavar='', type=str, help='TXT input file containing the message to process.  Default is message.txt if empty')

    generate_key(255, cipher_key)

if __name__ == "__main__":
    main()