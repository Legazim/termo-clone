import random
import unidecode
from valid_words import valid_words

CHOSEN_WORD_RAW = random.choice(valid_words)
CHOSEN_WORD = unidecode.unidecode(CHOSEN_WORD_RAW)
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

    def __init__(self, w_str: str) -> None:
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ''

    def next_turn(self):
        GuessWord.turn += 1

    def is_valid(self):
        return self.w_str in valid_words

    def apply_greens(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = unidecode.unidecode(CHOSEN_WORD[i])
            guessed_char = unidecode.unidecode(self.w_chars[i])
            if (actual_char == guessed_char):
                colored_char = f'{Color.GREEN}{actual_char}{Color.BASE}'
                self.w_chars[i] = colored_char

    def apply_guesses(self):
        self.apply_greens()
        self.post_guess_w_str = "".join(self.w_chars)
        print(self.post_guess_w_str)
