import random

global word_bank
word_bank = {0: "abruptly", 1: "bagpipes", 2: "cycle", 3: "dizzying"}

class hangman_game:

    #return string from the word bank randomly from key 0 to the amount of keys in the dictionary
    def generate_answer():
        word_bank_size = len(word_bank) - 1
        answer_string = word_bank[random.randint(0, word_bank_size)]
        return answer_string

    def generate_picture(wrong_guesses_left):
        picture = ""
        if wrong_guesses_left == 7:
            picture = "\n\n\n\n\n"
        elif wrong_guesses_left == 6:
            picture = "\t\t   |---\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "_____________________"
        elif wrong_guesses_left == 5:
            picture = "\t\t   |---\t\t\n"\
                       "\t\t   O  |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "_____________________"
        elif wrong_guesses_left == 4:
            picture = "\t\t   |---\t\t\n"\
                       "\t\t   O  |\t\t\n"\
                       "\t\t   |  |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "_____________________"
        elif wrong_guesses_left == 3:
            picture = "\t\t   |---\t\t\n"\
                       "\t\t   O  |\t\t\n"\
                       "\t\t   |  |\t\t\n"\
                       "\t\t   \  |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "_____________________"
        elif wrong_guesses_left == 2:
            picture = "\t\t   |---\t\t\n"\
                       "\t\t   O  |\t\t\n"\
                       "\t\t   |  |\t\t\n"\
                       "\t\t  /\  |\t\t\n"\
                       "\t\t      |\t\t\n"\
                       "_____________________"
        elif wrong_guesses_left == 1:
            picture = "\t\t   |---\t\t\n" \
                       "\t\t   O  |\t\t\n" \
                       "\t\t   |\ |\t\t\n" \
                       "\t\t  /\  |\t\t\n" \
                       "\t\t      |\t\t\n" \
                       "_____________________"
        elif wrong_guesses_left == 0:
            picture = "\t\t   |---\t\t\n" \
                       "\t\t   O  |\t\t\n" \
                       "\t\t  /|\ |\t\t\n" \
                       "\t\t   /\ |\t\t\n" \
                       "\t\t      |\t\t\n" \
                       "_____________________"
        print(picture)

    def generate_dictionary_answer(answer):
        answer_dictionary = {}
        for key in range(len(answer_string)):
            if answer_string[key] in answer_dictionary.keys():
                answer_dictionary[answer_string[key]].append(key)
            else:
                answer_dictionary[answer_string[key]] = [key]
        return answer_dictionary

    # def setup_game():
answer_string = hangman_game.generate_answer()
answer_dictionary = hangman_game.generate_dictionary_answer(answer_string)
shown_answer = ['_'] * len(answer_string)
wrong_guesses_left = 7
wrong_guesses = []
game_over = False
while not game_over:
    print(shown_answer)
    player_guess = input("You have " + str(wrong_guesses_left) + " guess(es) left.\t\t").lower()
    if player_guess in answer_dictionary:
        for value in answer_dictionary[player_guess]:
            shown_answer[value] = player_guess
    else:
        wrong_guesses_left -= 1
        wrong_guesses.append(player_guess)
    hangman_game.generate_picture(wrong_guesses_left)
    if wrong_guesses_left <= 0:
        game_over = True
        print("You lost! The answer was:\n" + str(answer_string))
    if "_" not in shown_answer:
        print(shown_answer)
        print("You win!")
        game_over = True