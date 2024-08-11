import pyautogui
import time
import random

# 0.007,0.3,0.85 on 35 WPM on morse.halb.it

WPM_SCALE,RANDOM_THINKING,DELIBERATE_SPACE = 0.007,0.3,0.85
# WPM_SCALE,RANDOM_THINKING,DELIBERATE_SPACE = 0.007,0,0
DASH_MAX_LENGTH = 1
TYPO_CHANCE = 0.01
HH_PROSIGN = True
DELIBERATE_TYPO = True

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/', ':': '---...', '\'': '.----.',
}

def string_to_morse(message):
    morse_message = ''
    for char in message.upper():
        morse_character = MORSE_CODE_DICT.get(char)
        if morse_character:
            morse_message += morse_character + ' '
        elif char == ' ':
            morse_message += '/ '
    return morse_message

def morse_clicker(morse_message):
    # print([*morse_message])
    is_typo = False
    index_before_last_space = 0
    index = 0
    listed_morse_message = [*morse_message]
    listed_morse_message.append('/')
    print(listed_morse_message)
    while index < len(listed_morse_message):
        symbol = listed_morse_message[index]
        if random.random() < TYPO_CHANCE and DELIBERATE_TYPO:
            symbol = '-' if symbol == '.' else '.'
            is_typo = True
            print("typo")
        if symbol == ".":
            if bool(random.random() < 0.1):
                # pyautogui.click()
                pyautogui.press('space')
            else:
                # pyautogui.mouseDown(button='left')
                pyautogui.keyDown('space')
                time.sleep(random.uniform(0,0.3*WPM_SCALE))
                # pyautogui.mouseUp(button='left')
                pyautogui.keyUp('space')
        elif symbol == "-":
            # pyautogui.mouseDown(button='left')
            pyautogui.keyDown('space')
            time.sleep(0.6*WPM_SCALE)
            time.sleep(random.uniform(0,DASH_MAX_LENGTH))
            # pyautogui.mouseUp(button='left')
            pyautogui.keyUp('space')
        elif symbol == "/":
            time.sleep(1*WPM_SCALE)
            time.sleep(random.uniform(RANDOM_THINKING,1))
            if is_typo:
                is_typo = False
                # HH Prosign
                if HH_PROSIGN:
                    for _ in range(8):
                        pyautogui.keyDown('space')
                        pyautogui.keyUp('space')
                # redo the word
                index = index_before_last_space 
                time.sleep(1*WPM_SCALE)
                time.sleep(random.uniform(RANDOM_THINKING,1))
            index_before_last_space = index
        elif symbol == " ":
            time.sleep(0.7*WPM_SCALE)
            time.sleep(random.randrange(18,25)*DELIBERATE_SPACE*WPM_SCALE)
        index += 1

message = "hi"
morse_message = string_to_morse(message)
print(f"Morse code: {morse_message}")
time.sleep(3)
morse_clicker(morse_message)