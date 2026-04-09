def has_player_won(secret_word, letters_guessed):
    return all(char in letters_guessed for char in secret_word)

secret = "wildcard"
guessed = ['k', 'w', 'i', 'l', 'd', 'c', 'r', 'a']
print(f"Secret: {secret}")
print(f"Guessed: {guessed}")
print(f"Result: {has_player_won(secret, guessed)}")
