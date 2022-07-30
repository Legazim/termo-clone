import termo

if __name__ == '__main__':
    with open('cheat.txt', 'w', encoding='UTF-8') as f:
        f.write(termo.CHOSEN_WORD_RAW)
    while True:
        guess = termo.GuessWord(
            w_str=input(f'{termo.GuessWord.turn} / {termo.GUESSES_COUNT} > ')
        )
        if guess.is_valid():
            guess.apply_guesses()
            guess.next_turn()
