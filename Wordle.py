import random

words = ["alma", "buza", "geci", "szek", "negy"]

generated_word = random.choice(words)


user_attemp = 0
total_attemp = 5

first_gen = generated_word[0]
second_gen = generated_word[1]
third_gen = generated_word[2]
fourth_gen = generated_word[3]


print("Szia ez egy Wordle-hoz hasonlo game,\n4 betus szavakat kell kitalálnod, 6 probalkozasod van!")

while user_attemp < total_attemp:
    ask_word = input("Enter the guessed word: ")

    first_ask = ask_word[0]
    second_ask = ask_word[1]
    third_ask = ask_word[2]
    fourth_ask = ask_word[3]


    
    user_attemp += 1
    
    if first_ask == first_gen and second_ask == second_gen and third_ask == third_gen and fourth_ask == fourth_gen:
        print("The word is {}.".format(generated_word))
        print("Wow you guessed it within {} attempt(s)".format(user_attemp))
        break

         
