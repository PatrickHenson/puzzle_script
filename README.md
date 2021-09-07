# puzzle_script
Generate 'encrypted' messages for use in tabletop RPGs.

This project exists to create encrypted messages, using a substitution cipher, for use in tabletop roleplaying games.  Players can either be given a series of messages to solve on their own or provided with the key.

The output is stored in multiple formats to make it easy to utilize.
**log.txt**
* RANDOM SEED: the value used to generate the substitution cipher.
* MESSAGE: the original input message.
* ENCODED MESSAGE: the message generated by the substitution cipher.
* CIPHER KEY: the key that can be used to translate the encoded message.
**original_message.jpg**
* The original message rendered using a custom RPG inspired font.
**encoded_message.jpg**
* The encoded message rendered using a custom RPG inspired font.
**alphabet.jpg**
* Reference that can be used to translate between the standard alphabet and custom RPG inspired font.

# Usage
**Simple use:**
1. Store your message(s) in a file named 'message.txt' in the same directory as puzzle_script.py
2. Execute the command to run the program
```
python3 puzzle_script.py
```
3. View the generated output

# Required Dependencies
```
# install pip3
sudo apt install python3-pip
python3 -m pip install --upgrade pip

# install virtualenv
pip3 install virtualenv
virtualenv --python=python3 env_name

# create virtualenv for python3
which python3
python3 -m pip virtualenv -p /usr/bin/python3 venv
source venv/bin/activate

# install Pillow
python3 -m pip install --upgrade Pillow
```

# Fonts
Tuigan Font 
* Designed by Pixel Sagas
* Licensed as Freeware
* https://www.fontspace.com/tuigan-font-f20523