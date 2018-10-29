#!/usr/bin/env python3

from pynput import keyboard
import sys


textToType = 'Hello. Let\'s start typing to improve typing skills.'
idxToType = 0
lineWidth = len(textToType) + 2

print('Text to type:')
print(textToType)


def getNextChar():
    return textToType[idxToType]


def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def on_press(key):
    key_name = get_key_name(key)
    nextChar = getNextChar()
    if (key_name == nextChar or (key_name == 'Key.space' and nextChar == ' ')):
        global idxToType
        idxToType += 1

        if len(textToType) == idxToType:
            printStatus()
            print('Done!')
            return False
    printStatus()


def printStatus():
    print('\r{0}'.format(textToType[:idxToType].ljust(lineWidth, ' ')), end='')


def on_release(key):
    key_name = get_key_name(key)    

    if key_name == 'Key.esc':
        print('Exiting...')
        return False


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
