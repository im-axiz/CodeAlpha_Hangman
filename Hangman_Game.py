#Aziz Ahmad
#CodeAlpha task 1
#Hangman game

import random
import time
import sys

class HangmanGame:
    def __init__(self, user_name, user_age, level):
        self.user_name = user_name
        self.user_age = user_age
        self.level = level
        self.total_score = 0
        self.prev_words = []
        self.start_time = time.time()
        self.categories = {
            "Programming Language": ("python", "java", "swift", "javascript", "hangman", "programming"),
            "Fruit": ("banana", "mango", "apple", "grapes", "pineapple"),
            "Animal": ("rabbit", "monkey", "donkey", "elephant", "lion", "giraffe", "cow"),
            "Vehicle": ("car", "aeroplane", "jet"),
            "Country": ("pakistan", "germany", "japan", "brazil"),
            "Movie": ("inception", "titanic", "avatar", "joker"),
            "Famous Person": ("einstein", "newton", "tesla", "galileo")
        }
        self.max_incorrect_guesses = 5

    def choose_word(self):
        if self.level == "easy":
            print(":::::CATEGORY SELECTION:\n[1 for Fruit]\n[2 for Programming Language]\n[3 for Animal]\n[4 for Vehicle]\n[5 for Country]\n[6 for Movie]\n[7 for Famous Person]")
            category_choice = input("Choose a category:")
            category_map = {
                '1': "Fruit", '2': "Programming Language", '3': "Animal",
                '4': "Vehicle", '5': "Country", '6': "Movie", '7': "Famous Person"
            }
            category = category_map.get(category_choice)
            if category:
                word = random.choice(self.categories[category])
            else:
                print("Invalid choice. Randomly selecting a category.")
                category, word_list = random.choice(list(self.categories.items()))
                word = random.choice(word_list)
        else:
            category, word_list = random.choice(list(self.categories.items()))
            word = random.choice(word_list)

        while word in self.prev_words:
            category, word_list = random.choice(list(self.categories.items()))
            word = random.choice(word_list)
        
        self.prev_words.append(word)
        return word, category

    def display_word(self, word, guessed_letters):
        return " ".join([letter if letter in guessed_letters else "_" for letter in word])

    def is_word_guessed(self, word, guessed_letters):
        return all(letter in guessed_letters for letter in word)

    def play(self):
        word, category = self.choose_word()
        guessed_letters = []
        incorrect_guesses = 0
        round_score = 0
        hint_count = 0
        max_hints = 2 if self.level in ["easy", "medium"] else 0
        word_start_time = time.time()
        while incorrect_guesses < self.max_incorrect_guesses:
            print("Word: " + self.display_word(word, guessed_letters))
            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                round_score += 10
                print("Good guess! Your Score increased by 10; Updated Score:", round_score)
            else:
                guessed_letters.append(guess)
                incorrect_guesses += 1
                round_score -= 5
                print(f"Incorrect guess. You have {self.max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
                print("Your Score decreased by 5; Updated Score:", round_score)

                if hint_count < max_hints:
                    x = input("Want a hint? \nA hint will cost you 5 points (Y/N): ")
                    if x.lower() == 'y':
                        hint_count += 1
                        if self.level == "easy":
                            revealed_letter = random.choice([letter for letter in word if letter not in guessed_letters])
                        elif self.level == "medium" and hint_count == 1:
                            revealed_letter = random.choice([letter for letter in word if letter not in guessed_letters])
                        elif self.level == "medium" and hint_count == 2:
                            print(f"Hint: The word is a {category}.")
                            revealed_letter = None
                        if revealed_letter:
                            print(f"Hint: The word contains the letter '{revealed_letter}'.")
                            guessed_letters.append(revealed_letter)
                        round_score -= 5
                        print("Your Score decreased by 5; Updated Score:", round_score)

            if self.is_word_guessed(word, guessed_letters):
                print(f"\nCongratulations! You guessed the word: {word}")
                self.total_score += round_score
                print(f"Your total score is: {self.total_score}")
                break
        else:
            print(f"\nGame over. The word was: {word}")

        word_end_time = time.time()
        word_time_taken = word_end_time - word_start_time
        print(f"Time Taken: {int(word_time_taken // 60)} minutes and {int(word_time_taken % 60)} seconds.")

    def log_history(self):
        end_time = time.time()
        total_time = end_time - self.start_time
        with open("history.txt", "a") as history_file:
            history_file.write(f"Name: {self.user_name}, Age: {self.user_age}, Score: {self.total_score}, Time Played: {int(total_time // 60)} minutes and {int(total_time % 60)} seconds\n")

    def run(self):
        while True:
            self.play()
            play_again = input("\nDo you want to play again? (Y/N): ")
            if play_again.lower() != 'y':
                print("Exiting", end="")
                for _ in range(3):
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    time.sleep(0.5)
                print(f"\nThank you for playing, {self.user_name}!")
                print(f"Your final score is: {self.total_score}")
                self.log_history()
                time.sleep(1)
                break

if __name__ == "__main__":
    print("\nWelcome to Hangman!")
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    print(":::::LEVEL SELECTION\n[E / e / 1 for Easy]\n[M / m / 2 for Medium]\n[H / h / 3 for Hard]")
    level_choice = input("Choose a level: ").lower()
    level_map = {'1': 'easy', 'e': 'easy', '2': 'medium', 'm': 'medium', '3': 'hard', 'h': 'hard'}
    level = level_map.get(level_choice, 'medium')
    game = HangmanGame(user_name, user_age, level)
    game.run()
