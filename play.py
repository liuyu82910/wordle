from wordle import Wordle
from checkletter import CheckLetter
from colorama import Fore, Back, Style
from typing import List
from random import choice
import enchant


def main():
    d = enchant.Dict("en_US")
    print("welcome 2 wordle")
    origin_word = load_word('five_letter_words.txt')
    picked_word = choice(list(origin_word))
    word = Wordle(picked_word)
    duplicate = []
    while word.check_attempts:
        while True:
            guess = input("\nPlease input your guess: ")
            if guess not in duplicate:
                duplicate.append(guess)
                break
            else:
                print(Fore.MAGENTA + f'duplicate word {guess}, try again' + Fore.RESET)
        if len(guess) != word.LENGTH or not guess.isalpha():
            print(Fore.MAGENTA + 'please enter a 5-letter word, no numbers' + Fore.RESET)
            continue
        if not d.check(guess):
            print(Fore.BLUE + 'This is not an English word' + Fore.RESET)
            continue
        word.attempt(guess)
        display_result(word)
    if word.won:
        print(f'You nailed the game, the word is {guess}')
    else:
        print(f'Sorry you failed, the word is {word.secret}')

def load_word(path: str):
    word_set = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            w = line.strip()
            word_set.add(w)
    return word_set   

def display_result(wordle: Wordle):
    print(f'\nYou have {wordle.attempts_balance} attempt(s) remaining\n')
    for word in wordle.attempts:
        result = wordle.compare(word)
        colored_result = convert_color(result)
        print(colored_result)   
    for _ in range(wordle.attempts_balance):
        print(' '.join('_' * Wordle.LENGTH))
        
def convert_color(result: List[CheckLetter]):
    result_with_color = []
    for letter in result:
        if letter.in_position:
            color = Fore.GREEN + Style.BRIGHT
        elif letter.in_word:
            color = Fore.RED + Style.BRIGHT
        else:
            color = Fore.WHITE + Style.BRIGHT
        colored_letter = color + letter.character + Fore.RESET + Style.RESET_ALL
        result_with_color.append(colored_letter)
    return ' '.join(result_with_color) 
    
if __name__ == "__main__":
    main()