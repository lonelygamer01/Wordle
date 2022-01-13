import random

words = ["alma", "buza", "geci", "fasz", "szek", "negy", "eger", "toll"]

generated_word = random.choice(words)


user_attempt = 0
total_attempt = 10

first_gen = generated_word[0]
second_gen = generated_word[1]
third_gen = generated_word[2]
fourth_gen = generated_word[3]


print("Szia ez egy Wordle-hoz hasonlo game,\n4 betus szavakat kell kitalálnod, 6 probalkozasod van!")

while user_attempt < total_attempt:
    ask_word = input("Enter the guessed word: ")

    first_ask = ask_word[0]
    second_ask = ask_word[1]
    third_ask = ask_word[2]
    fourth_ask = ask_word[3]


    
    user_attempt += 1
    
    if (first_ask == first_gen and second_ask == second_gen and third_ask == third_gen and fourth_ask == fourth_gen):
        print("The word is {}.".format(generated_word))
        print("All the letters in the word are on the right place!")
        print("Wow you guessed it within {} attempt(s)".format(user_attempt))
        break


    elif (first_ask == first_gen and second_ask == second_gen and third_ask == third_gen) or (first_ask == first_gen and second_ask == second_gen and fourth_ask == fourth_gen) or (first_ask == first_gen and third_ask == third_gen and fourth_ask == fourth_gen) or (second_ask == second_gen and third_ask == third_gen and fourth_ask == fourth_gen):
        print("Only 3 letters are correct!")

        if first_ask == first_gen and second_ask == second_gen and third_ask == third_gen:
            print("The {} , {} and {} letters are on the right place".format(first_gen, second_gen, third_gen))

        if first_ask == first_gen and second_ask == second_gen and fourth_ask == fourth_gen:
            print("The {} , {} and {} letters are on the right place".format(first_gen, second_gen, fourth_gen))

        if first_ask == first_gen and third_ask == third_gen and fourth_ask == fourth_gen:
            print("The {} , {} and {} letters are on the right place".format(first_gen, third_gen, fourth_gen))

        if second_ask == second_gen and third_ask == third_gen and fourth_ask == fourth_gen:
            print("The {} , {} and {} letters are on the right place".format(second_gen, third_gen, fourth_gen))



    elif (first_ask == first_gen and second_ask == second_gen) or (first_ask == first_gen and third_ask == third_gen) or (first_ask == first_gen and fourth_ask == fourth_gen) or (second_ask == second_gen and third_ask == third_gen) or (second_ask == second_gen and fourth_ask == fourth_gen) or (third_ask == third_gen and fourth_ask == fourth_gen):
        print("Only 2 letters are correct!")

        if first_ask == first_gen and second_ask == second_gen:
            print("The {} and {} are on the right place".format(first_gen, second_gen))

        if first_ask == first_gen and third_ask == third_gen:
            print("The {} and {} are on the right place".format(first_gen, third_gen))

        if first_ask == first_gen and fourth_ask == fourth_gen:
            print("The {} and {} are on the right place".format(first_gen, fourth_gen))

        if second_ask == second_gen and third_ask == third_gen:
            print("The {} and {} are on the right place".format(second_gen, third_gen)) 


        if second_ask == second_gen and fourth_ask == fourth_gen:
            print("The {} and {} are on the right place".format(second_gen, fourth_gen))

        if third_ask == third_gen and fourth_ask == fourth_gen:
            print("The {} and {} are on the right place".format(third_gen, fourth_gen))


    elif first_ask == first_gen or second_ask == second_gen or third_ask == third_gen or fourth_ask == fourth_gen:
        print("Only one letter is correct!")

        if first_ask == first_gen:
            print("The {} is on the right place".format(first_gen))

        if second_ask == second_gen:
            print("The {} is on the right place".format(second_gen))

        if third_ask == third_gen:
            print("The {} is on the right place".format(third_gen))

        if fourth_ask == fourth_gen:
            print("The {} is on the right place".format(fourth_gen))



    else:
        print("None of the letter are correct\nTry again later!")  
       
   

         
