import random

def hangman_game():
    words = ["aeroplane", "butter", "color", "door", "elephant"]
    secret_word = random.choice(words)  
    print("Hey! Welcome to Hangman Game!")
    print("Find the Secret Word.")
    print("You only get 6 wrong guesses. Good luck!")
    print('-'*20)

    right_letter = []
    wrong_letter = []
    wrong_count = 0
    wrong_limit = 6
    word_count = ["_"] * len(secret_word)
    
    print(f"Word has {len(secret_word)} letters: {' '.join(word_count)}")
    print()    
    
    while (wrong_count < wrong_limit) and ("_" in word_count):
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Oops! Please enter just one letter.\n")
            continue
        
        if guess in right_letter:
            print(f"You already guessed '{guess}'! Try another.\n")
            continue

        if guess in wrong_letter:
            wrong_count += 1
            print(f"You already tried '{guess}' and it was wrong!")
            print(f"Wrong guesses: {wrong_count}/{wrong_limit}\n")
            continue

        if guess in secret_word:
            right_letter.append(guess)
            print("Awesome! '{guess}' is correct!\n")
            
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_count[i] = guess
        else:
            wrong_letter.append(guess)
            wrong_count += 1
            print(f"'{guess}' is not in the word. Try again!")
            print(f"Wrong guesses: {wrong_count}/{wrong_limit}\n")
        
        print(f"Word: {' '.join(word_count)}")

        if right_letter:
            print(f"Correct letters: {', '.join(right_letter)}\n")
        
        if wrong_letter:
            print(f"Wrong letters: {', '.join(wrong_letter)}\n")
        
        print('-'*20)

    if "_" not in word_count:
        print(f"Congratulations! You won!")
        print(f"You made {len(wrong_letter)} wrong guesses.")
    else:
        print(f"Game over! You've used all your guesses. You can try again!")
        print(f"You correctly guessed {len(right_letter)} letters.")
    
    print(f"The word was: {secret_word}")

if __name__ == "__main__":
    hangman_game()