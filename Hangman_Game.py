from random import choice

words = ["python", "apple", "computer", "hangman", "programming"]
correct_letters =[]
incorrect_letters = []
tries = 6
right_answer = 0
game_over = False

def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))
    return chosen_word , different_letters

def ask_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while not is_valid:
        chosen_letter = input("Please enter a letter: ")

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You have not chosen a correct letter.")
    return chosen_letter

def show_board(chosen_word):
    my_list = []
    for l in chosen_word:
        if l in correct_letters:
            my_list.append(l)
        else:
            my_list.append('-')

    print(' '.join(my_list))


def check_letter(chosen_letter, hidden_word, tries, matches):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        matches += 1
    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1

    if tries == 0:
        end = lose()
    elif matches == unique_letter:
        end = win(hidden_word)

    return tries, end, matches

def lose():
    print("You have no tries left.")
    print("The hidden word was " + word)
    return True

def win(revealed_word):
    show_board(revealed_word)
    print("Congratulations, you have guessed the word!!!!")
    return True


word , unique_letter = choose_word(words)

while not game_over:
    print('\n' + '*' * 20 + '\n')
    show_board(word)
    print('\n')
    print("Incorrect letters: " + ','.join(incorrect_letters))
    print(f"Tries: {tries}")
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    tries, over, right_answer = check_letter(letter, word, tries, right_answer)
    game_over = over




