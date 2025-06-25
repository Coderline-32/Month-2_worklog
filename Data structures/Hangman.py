import random
words = ['Programming', 'Python', 'Coding']
    
word = random.choice(words).lower()
guesses = 0
print("""Welcome to the Hangman game!
      Instructions:
       >Guess the letter to fill in blank spaces. 
       >You have  6 attempts per wrong guess
       
      Hint:
       >The words are derived from Tech field
      Good luck playing the game!
      """)
        
def hint_for_word():
    
    reveal_indices = random.sample(range(len(word)), 2)
    display = [char if i in reveal_indices else '_' for i, char in enumerate(word)]
    display_2 = ''.join(display)
    print(display_2)
    return display

def match_letter(display, guesses):
    while guesses < 6:
        guess_letter = input("Guess the letter: ").lower()
        if not guess_letter.isalpha() or len(guess_letter) != 1:
            print("Enter valid letter from a-z: ")
        if guess_letter in word:
            for i, char in enumerate(word):
                if char == guess_letter:
                    display[i] = guess_letter
            print(''.join(display))
                   
                    
        else:
            guesses += 1  
            print(f"Wrong! Attempts left: {6 - guesses}")
            
        if ''.join(display) == word:
            print(f"You succesfully guessed {word}")
            break
    else:
            print(f"You ran out of guesses! The word was {word}")

def play_game():
    display = hint_for_word()
    match_letter(display, guesses)

while True:
    play_game()
    Replay_inquiry = input("Do you want to play the game again! (yes/no): ").lower()
    if Replay_inquiry != "yes":
        break





