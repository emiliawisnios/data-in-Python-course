# we are using Morse code signs for polish letters

letter_to_morse = {
    'a': '.-', 'ą': '.-.-', 'b': '-...', 'c': '-.-.',
    'ć': '-.-..', 'd': '-..', 'e': '.', 'ę': '..-..',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'ł': '.-..-',
    'm': '--', 'n': '-.', 'o': '---', 'ó': '---.',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
    'ś': '...-...', 't': '-', 'u': '..-', 'v': '...-',
    'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    'ż': '--..-.', 'ź': '--..-', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ''
    }


morse_to_letter = {value: key for key, value in letter_to_morse.items()}

MC_separator = '/'


def encrypting(message):
    # encrypting message to Morse code
    clean_message = message.strip().lower()  # deleting all white signs from the beginning and the end of string
    result = MC_separator.join(letter_to_morse[letter] for letter in clean_message)
    return result


def decrypting(message):
    # decrypting message from Morse code
    clean_message = message.strip()  # deleting all white signs from the beginning and the end of string
    result = ''.join(
        morse_to_letter[code]
        for code in clean_message.split(MC_separator)
    )
    return result.capitalize()  # we assume that first letter of message is always capital


def decryption_or_encryption():
    # function which interacts with the user
    to_continue = 'Y'
    while to_continue == 'Y':
        answer = input(f'Do you want to decrypt or encrypt your message? D/E').strip()
        message = input(f'What is your message?')
        if answer == 'D':
            result = decrypting(message)
            print(f'Your message is: {result}')
            to_continue = input(f'Do you want to continue? Y/N').strip()
        elif answer == 'E':
            result = encrypting(message)
            print(f'Your message is: {result}')
            to_continue = input(f'Do you want to continue? Y/N').strip()
        else:
            to_continue = input(f'Sorry, there is no such command. Do you want to continue? Y/N').strip()
    print(f'Thank you! See you again!')


decryption_or_encryption()
