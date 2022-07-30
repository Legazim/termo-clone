import random
import unidecode
from valid_words import valid_words
import sys

CHOSEN_WORD_RAW = random.choice(valid_words)
CHOSEN_WORD = unidecode.unidecode(CHOSEN_WORD_RAW).lower()
GUESSES_COUNT = 6


class Color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PERSISTENT_COLORS = [RED, GREEN]


class GuessWord:
    turn = 1
    past_guesses = []

    def __init__(self, w_str: str) -> None:
        self.w_str = w_str.lower()
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ''

    def next_turn(self):
        GuessWord.turn += 1

    def is_valid(self):
        if (self.w_str in valid_words):
            return True
        if (self.w_str == '-h'):
            self.call_guesses()
            return False
        else:
            return False

    def apply_yellows(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = unidecode.unidecode(self.w_chars[i])
            if (guessed_char in CHOSEN_WORD):
                colored_char = f'{Color.YELLOW}{guessed_char}{Color.BASE}'
                self.w_chars[i] = colored_char

    def apply_greens(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = unidecode.unidecode(CHOSEN_WORD[i])
            guessed_char = unidecode.unidecode(self.w_chars[i])
            if (actual_char == guessed_char):
                colored_char = f'{Color.GREEN}{actual_char}{Color.BASE}'
                self.w_chars[i] = colored_char

    def apply_guesses(self):
        self.apply_greens()
        self.apply_yellows()
        self.post_guess_w_str = "".join(self.w_chars)
        GuessWord.past_guesses.append(self.post_guess_w_str)
        print(self.post_guess_w_str)

    def call_guesses(self):
        print('\n::.......::')
        for element in GuessWord.past_guesses:
            print(f':. {element} ::')
        print('::.......::')

    def check_victory(self):
        if (self.w_str == CHOSEN_WORD or self.w_str == CHOSEN_WORD_RAW):
            print('::.:......................:.::')
            print(f'Parabéns!\nVocê venceu em {GuessWord.turn} tentativa(s)')
            print('::.:......................:.::')
            self.call_guesses()
            sys.exit(1)

    def check_loss(self):
        if (GuessWord.turn == GUESSES_COUNT):
            print('::.:......................:.::')
            print(
                f'Acabaram as suas chances!\nA palavra era {CHOSEN_WORD_RAW}'
            )
            print('::.:......................:.::')
            self.call_guesses()
            sys.exit(1)
