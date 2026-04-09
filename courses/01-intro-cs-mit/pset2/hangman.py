# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # Trận pháp: Kiểm tra xem mọi linh ấn trong secret_word đều đã nằm trong letters_guessed chưa
    return all(char in letters_guessed for char in secret_word)


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # Trận pháp: Duyệt qua từ bí mật, nếu thấy linh ấn đã đoán thì hiện, ngược lại dấu bằng '*'
    return "".join(char if char in letters_guessed else "*" for char in secret_word)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # Trận pháp: Loại bỏ các chữ cái đã đoán khỏi bảng Alphabet (a-z)
    alphabet = string.ascii_lowercase
    return "".join(char for char in alphabet if char not in letters_guessed)


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.
    """
    guesses_left = 10
    letters_guessed = []
    hints_used = 0
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_left > 0:
        print("------")
        # Xử lý số ít/số nhiều cho linh lực
        guess_str = "guess" if guesses_left == 1 else "guesses"
        print(f"You have {guesses_left} {guess_str} left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        user_input = input("Please guess a letter: ").lower()
        
        # Hóa giải chế độ Cầu cứu (Help Mode)
        if with_help and user_input == "!":
            if guesses_left < 3:
                print(f"Oops! Not enough guesses for a hint: {get_word_progress(secret_word, letters_guessed)}")
            else:
                # Ghi nhận dùng Hint và trừ linh lực ngay
                hints_used += 1
                guesses_left -= 3
                
                missing_letters = [char for char in secret_word if char not in letters_guessed]
                if missing_letters:
                    revealed = random.choice(missing_letters)
                    letters_guessed.append(revealed)
                    print(f"Letter revealed: {revealed}")
                    print(f"{get_word_progress(secret_word, letters_guessed)}")
                
                # Kiểm tra thắng lợi sau khi đã trừ linh lực
                if has_player_won(secret_word, letters_guessed):
                    print("------")
                    print("Congratulations, you won!")
                    unique_total = len(set(secret_word))
                    total_score = (guesses_left + 4 * unique_total) + (3 * len(secret_word))
                    print(f"Your total score for this game is: {total_score}")
                    return
            continue

        # Kiểm tra tính hợp lệ của linh ấn
        if len(user_input) != 1 or user_input not in string.ascii_lowercase:
            print(f"Oops! That is not a valid letter: {get_word_progress(secret_word, letters_guessed)}")
            continue
            
        if user_input in letters_guessed:
            print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            continue
            
        letters_guessed.append(user_input)
        
        if user_input in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
            
            if has_player_won(secret_word, letters_guessed):
                print("------")
                print("Congratulations, you won!")
                unique_total = len(set(secret_word))
                total_score = (guesses_left + 4 * unique_total) + (3 * len(secret_word))
                print(f"Your total score for this game is: {total_score}")
                return
        else:
            # Hình phạt tiêu hao linh lực khi đoán sai
            if user_input in "aeiou":
                guesses_left -= 2
            else:
                guesses_left -= 1
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

    print("------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

