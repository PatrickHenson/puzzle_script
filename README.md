# puzzle_script
Generate 'encrypted' messages for use in tabletop RPGs.

This project exists to create encrypted messages, using a substitution cipher, for use in tabletop roleplaying games.  Players can either be given a series of messages to solve on their own or provided with the key.

Input:
* message - the message you would like to use
* options - ...apply cipher, random_seed, font, etc

Output:
* cipher_key - cipher key
* message - the encrypted message

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