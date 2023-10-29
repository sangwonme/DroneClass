from djitellopy import Tello
import time

# create and connect
tello = Tello()
tello.connect()

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}

def show_dot_line(morse):
    # TODO : .이 들어오면 깜박. -이 들어오면 깜-박
    if morse == '.':
        time.sleep(0.3)
        tello.send_expansion_command("led 255 0 0")
        time.sleep(0.5)
        tello.send_expansion_command("led 0 0 0")
    elif morse == '-':
        time.sleep(0.3)
        tello.send_expansion_command("led 255 0 0")
        time.sleep(1)
        tello.send_expansion_command("led 0 0 0")
    pass

def word_to_morse(word):
    # word = ['A', 'P', 'P', 'L', 'E']
    # for i in range(len(word))
    word = list(word)
    # TODO : 각각의 알파벳에 대해서 모스부호를 보낸다
    for i in range(len(word)):
      morses = list(morse_code[word[i]])
      for j in range(len(morses)):
          show_dot_line(morses[j])

while True:
    word = input()
    word_to_morse(word)
    