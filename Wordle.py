import random

words = ["alma", "buza", "geci", "szek, negy"]

generated_word = random.choice(words)


user_attemp = 0
total_attemp = 5

first = generated_word[0]
second = generated_word[1]
third = generated_word[2]
fourth = generated_word[3]




while user_attemp < total_attemp:
    ask_word = input("Enter the guessed word: ")
    
    user_attemp += 1
    if ask_word == generated_word:
        print("The word is {}.".format(generated_word))
        print("Wow you guessed it within {} attempt(s)".format(user_attemp))
        break
    else:
        print("Better luck next time")


       

