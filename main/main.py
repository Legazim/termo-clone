import termo
import os

begin_message = """\033[90m
'###########:'########:'########::'####::::'####:'.#######::
 :::'##: :::: ##.....:: ##.... ##: ##.##. ##. ##:'##.... ##:
 ::: ##: :::: ##::::::: ##:::: ##: ##:: ## :: ##: ##:::: ##:
 ::: ##: :::: ######::: ########:: ##:: ## :: ##: ##:::: ##:
 ::: ##: :::: ##...:::: ##.. ##::: ##:: ## :: ##: ##:::: ##:
 ::: ##: :::: ##::::::: ##::. ##:: ##:: ## :: ##: ##:::: ##:
.::: ##: :::. ########: ##:::. ##: ##:: ## :: ##: .#######::
:...::...::::........::..:::::..::........:::....:.......:::
\033[0m"""
os.system('cls') if os.name == 'nt' else os.system('clear')

print(begin_message.replace('#', f'{termo.Color.GREEN}#{termo.Color.GREY}'))
# print(termo.CHOSEN_WORD_RAW)

if __name__ == '__main__':
    while True:
        guess = termo.GuessWord(w_str=input(
                    f'{termo.GuessWord.turn} / {termo.GUESSES_COUNT} > '
                ).upper())
        if guess.is_valid():
            guess.apply_guesses()
            guess.check_victory()
            guess.check_loss()
            guess.next_turn()
