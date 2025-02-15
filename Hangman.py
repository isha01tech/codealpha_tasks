import random

def get_word():
    words = ["india", "china", "japan", "france", "germany", "brazil", "canada", "egypt"]
    return random.choice(words)

def play(word):
    word_letters = set(word)  # Letters in the word
    alphabet = set(chr(i) for i in range(ord('a'), ord('z') + 1)) # All lowercase alphabets
    used_letters = set()  # What the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Letters used
        print('You have used these letters: ', ' '.join(used_letters))

        # Current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1  # Takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # Gets here when len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


if __name__ == "__main__":
    print("Welcome to Hangman!")
    word = get_word()
    play(word)
