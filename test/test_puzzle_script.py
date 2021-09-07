from puzzle_script.puzzle_script import decode_substitution_cipher, encode_substitution_cipher, generate_key, reverse_key
import sys
sys.path.append("../")

import pytest
from puzzle_script import *

# Test the generate_key function reliable creates the same key for the seed input.
def test_generate_key():
    expected_key = {
        'a': 'b', 'b': 'k', 'c': 'u', 'd': 'z', 'e': 's', 'f': 'l', 'g': 't', 'h': 'y', 'i': 'e', 'j': 'q', 'k': 'v', 
        'l': 'r', 'm': 'i', 'n': 'm', 'o': 'j', 'p': 'o', 'q': 'f', 'r': 'n', 's': 'c', 't': 'g', 'u': 'w', 'v': 'h', 
        'w': 'x', 'x': 'd', 'y': 'p', 'z': 'a'
    }
    cipher_key = generate_key(255)
    assert cipher_key == expected_key
    
def test_reverse_key():
    expected_key = {
        'b': 'a', 'k': 'b', 'u': 'c', 'z': 'd', 's': 'e', 'l': 'f', 't': 'g', 'y': 'h', 'e': 'i', 'q': 'j', 'v': 'k', 
        'r': 'l', 'i': 'm', 'm': 'n', 'j': 'o', 'o': 'p', 'f': 'q', 'n': 'r', 'c': 's', 'g': 't', 'w': 'u', 'h': 'v', 
        'x': 'w', 'd': 'x', 'p': 'y', 'a': 'z'
    }
    cipher_key = generate_key(255)
    reversed_key = reverse_key(cipher_key)
    assert reversed_key == expected_key

def test_encode_substitution_cipher():
    input_message = 'Hello World!'
    expected_message = 'ysrrj xjnrz'
    cipher_key = generate_key(255)
    encoded_message = encode_substitution_cipher(input_message, cipher_key)
    assert encoded_message == expected_message

def test_decode_substitution_cipher():
    input_message = 'ysrrj xjnrz'
    expected_message = 'hello world'
    cipher_key = generate_key(255)
    decoded_message = decode_substitution_cipher(input_message, cipher_key)
    assert decoded_message == expected_message