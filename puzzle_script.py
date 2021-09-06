import argparse
import os
import random
import string
import sys
from PIL import Image, ImageDraw, ImageFont

# Generate the cipher key using a set seed value.
# The generated key is stored as a dictionary with [key,value] pairs as [letter,substitution]
def generate_key(seed):
    # Track which letters have been used in the generated key.
    alphabet = string.ascii_lowercase
    alphabet_length = len(alphabet)
    letter_is_used = [False] * len(alphabet)

    # Seeding the random number generator allows the same key to be used for multiple messages.
    random.seed(seed)

    # Assign a unique replacement to each letter of the alphabet.
    cipher_key = {}
    for i in range(0, alphabet_length):
        substituted = False
        while not substituted:
            new_position = random.randint(0, alphabet_length-1)
            if not letter_is_used[new_position] and i is not new_position:
                cipher_key[alphabet[i]] = alphabet[new_position]
                letter_is_used[new_position] = True
                substituted = True
    return cipher_key

# Generate a new dictionary by reversing the [key,value] pairs of the key.
# This function is used for proof/testing and is not exposed.
def reverse_key(cipher_key):
    reversed_key = {}
    for k in cipher_key.keys():
        reversed_key[cipher_key[k]] = k
    return reversed_key

# Encode the message using the substitution cipher key.
# The encoded message will only contain lowercase letters.
def encode_substitution_cipher(message, cipher_key):
    encoded_message = ""
    for c in message.lower():
        if c in cipher_key.keys():
            encoded_message += cipher_key[c]
        else:
            encoded_message += c
    return encoded_message
    

# Decode the message using the substitution cipher key.
# This function is used for proof/testing and is not exposed.
def decode_substitution_cipher(message, cipher_key):
    reversed_key = reverse_key(cipher_key)
    decoded_message = ""
    for c in message.lower():
        if c in reversed_key.keys():
            decoded_message += reversed_key[c]
        else:
            decoded_message += c
    return decoded_message

# Generate image output 
def generate_image(message):
    # Create base image.
    image_size = (600,800)
    canvas = Image.new('RGB', image_size, 'white')
    # Load custom font and render message.
    font_file = os.path.abspath(os.getcwd()) + '/fonts/tuigan_font/Tuigan-KppX.ttf'
    font = ImageFont.truetype(font_file, size=14, encoding='unic')
    render = ImageDraw.Draw(canvas)
    render.text((10,10), message, 'black', font)

    # canvas.save('output_image.jpg')
    canvas.show()


# Processes command line input and execute the program.
def main(): 
    # Program description
    description_text='''
    Welcome to Puzzle Script - Substitution Cipher\n

    This code was developed to easily generate 'secret messages' for use in tabletop role playing games.  The output 
    can be given to players to decode on their own or the key can be provided to give them a head start.
    '''

    # Setup command line input
    parser = argparse.ArgumentParser(description=description_text)
    parser.add_argument(
        '-f', 
        dest='file_input',
        type=str,
        default='message.txt',
        help='Input file containing the message(s) to process.  Default is "message.txt".')
    parser.add_argument(
        '-s',
        dest='seed',
        type=int,
        required=False,
        help='Set the seed value to gaurantee the same random cipher key is used across multiple runs.'
    )
    
    # Parse command line input.
    args = parser.parse_args()
    
    # Read message from file.
    text_input = open(args.file_input, 'r')
    message = text_input.read()
    text_input.close()
    
    # Generate the substitution cipher key.
    seed = args.seed
    if seed is None:
        seed = random.randint(0, sys.maxsize)
    cipher_key = generate_key(seed)

    # Encode the message
    encoded_message = encode_substitution_cipher(message, cipher_key)

    # Generate image containing the message text.
    generate_image(encoded_message)

    # Output a file with process information.
    log = '## RANDOM SEED ##\n{}\n\n## MESSAGE ##\n{}\n\n## ENCODED MESSAGE ##\n{}\n\n'
    text_output = open('output.txt', 'w')
    text_output.write(log.format(seed, message, encoded_message))
    text_output.close()


if __name__ == "__main__":
    main()