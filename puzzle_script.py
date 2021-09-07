import argparse
import os
import random
import string
import sys
from PIL import Image, ImageDraw, ImageFont

# This is the custom font, provided in the repo, used to render output images.
# Replaces this variable if you want to use a load a different custom font.
font_file = os.path.abspath(os.getcwd()) + '/fonts/tuigan_font/Tuigan-KppX.ttf'

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
# The encoded message will only contain lowercase letters, spaces, and newlines.
def encode_substitution_cipher(message, cipher_key):
    encoded_message = ""
    for c in message.lower():
        if c in cipher_key.keys():
            encoded_message += cipher_key[c]
        elif c == ' ' or c == '\n':
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
        elif c == ' ' or c == '\n':
            decoded_message += c
    return decoded_message

# Generate image output 
def generate_image(message, file_out):
    # Load custom font.    
    custom_font = ImageFont.truetype(font_file, size=14, encoding='unic')
    
    # Determine canvas size from font properties and message content.
    image_padding = 10
    image_width, image_height = custom_font.getsize_multiline(message)
    image_width += image_padding * 2
    image_height += image_padding

    canvas = Image.new('RGB', (image_width, image_height), 'white')
    render = ImageDraw.Draw(canvas)

    x = 10 # pixel indent from left
    y = 10 # pixel indent from top
    for line in message.splitlines():
        render.text((x, y), line.rstrip(), 'black', custom_font)
        y += custom_font.size

    canvas.save(file_out)
    #canvas.show() # optionally show the image with or without saving

# Output a 'key file' to convert between ascii and custom font
def generate_alphabet_key():
    message = ''
    for c in string.ascii_lowercase:
        message += c + ' '

    default_font = ImageFont.load_default()
    custom_font = ImageFont.truetype(font_file, size=12, encoding='unic')
    
    canvas = Image.new('RGB', (325, 40), 'white')
    render = ImageDraw.Draw(canvas)
    render.text((10,10), message, 'black', default_font)
    render.text((10,20), message, 'black', custom_font)

    canvas.save('alphabet.jpg')
    #canvas.show() # optionally show the image with or without saving


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

    # Create a human readable key to translate the encoded message.
    reversed_key = reverse_key(cipher_key)
    output_key = {0:'', 1:''}
    for c in sorted(reversed_key.keys()):
        output_key[0] += c + ' '
        output_key[1] += reversed_key[c] + ' '

    # Encode the message
    encoded_message = encode_substitution_cipher(message, cipher_key)

    # Generate image files containing the message, encoded message, and alphabet key.
    generate_image(message, 'original_message.jpg')
    generate_image(encoded_message, 'encoded_message.jpg')
    generate_alphabet_key()

    # Output log file with information about the run.
    log = '## RANDOM SEED ##\n{}\n\n## MESSAGE ##\n{}\n\n## ENCODED MESSAGE ##\n{}\n\n## CIPHER KEY##\n{}\n{}\n\n'
    text_output = open('log.txt', 'w')
    text_output.write(log.format(seed, message, encoded_message, output_key[0], output_key[1]))
    text_output.close()


if __name__ == "__main__":
    main()