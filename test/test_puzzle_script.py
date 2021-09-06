from puzzle_script.puzzle_script import generate_key
import sys
sys.path.append("../")

import pytest
from puzzle_script import *

# Test the generate_key function reliable creates the same key for the seed input.
def test_generate_key():
    expected_key = {'a': 'b', 'b': 'k', 'c': 'u', 'd': 'z', 'e': 's', 'f': 'l', 'g': 't', 'h': 'y', 'i': 'e', 'j': 'q', 'k': 'v', 'l': 'r', 'm': 'i', 'n': 'm', 'o': 'j', 'p': 'o', 'q': 'f', 'r': 'n', 's': 'c', 't': 'g', 'u': 'w', 'v': 'h', 'w': 'x', 'x': 'd', 'y': 'p', 'z': 'a'}

    cipher_key = {}
    generate_key(255, cipher_key)
    assert cipher_key == expected_key
    