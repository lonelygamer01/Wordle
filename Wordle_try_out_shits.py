generated_word = "duck"

ask_word = input("Enter a word: ")

first_gen = generated_word[0]
second_gen = generated_word[1]
third_gen = generated_word[2]
fourth_gen = generated_word[3]

first_ask = ask_word[0]
second_ask = ask_word[1]
third_ask = ask_word[2]
fourth_ask = ask_word[3]




    

if (first_ask in generated_word) and (second_ask in generated_word) and (third_ask in generated_word) and (fourth_ask in generated_word):
    print("All of the letters are in the generated word!")


elif (first_ask and second_ask and third_ask) or (first_ask and second_ask and fourth_ask) or (first_ask and third_ask and fourth_ask) or (second_ask and third_ask and fourth_ask) in generated_word:
    
    if (first_ask and second_ask and third_ask) in generated_word:
        print("The {}, {}, {} letters are in the generated word!".format(first_ask, second_ask, third_ask))
                
    elif (first_ask and second_ask and fourth_ask) in generated_word:
        print("The {}, {}, {} letters are in the generated word!".format(first_ask, second_ask, fourth_ask))

    elif (first_ask and third_ask and fourth_ask) in generated_word:
        print("The {}, {}, {} letters are in the generated word!".format(first_ask, third_ask, fourth_ask))

    elif (second_ask and third_ask and fourth_ask) in generated_word:
        print("The {}, {}, {} letters are in the generated word!".format(second_ask, third_ask, fourth_ask))




elif (first_ask and second_ask) or (first_ask and third_ask) or (first_ask and fourth_ask) or (second_ask and third_ask) or (second_ask and fourth_ask) or (third_ask and fourth_ask) in generated_word:
    
    if (first_ask and second_ask) in generated_word:
        print('The {}, {} letters are in the generated word!'.format(first_ask, second_ask))

    elif (first_ask and third_ask) in generated_word:
        print('The {}, {} letters are in the generated word!'.format(first_ask, third_ask))

    elif (first_ask and fourth_ask) in generated_word:
        print('The {}, {} letters are in the generated word!'.format(first_ask, fourth_ask))

    elif (second_ask and third_ask) in generated_word:
        print('The {}, {} letters are in the generated word!'.format(second_ask, third_ask))

    elif (second_ask and fourth_ask) in generated_word:
        print('The {}, {} letters are in the generated word!'.format(second_ask, fourth_ask))

    elif (third_ask and fourth_ask) in generated_word:
        print('The {}, {} letters are in the generated word!'.format(third_ask, fourth_ask))




elif first_ask or second_ask or third_ask in generated_word or fourth_ask in generated_word:

    if first_ask  in generated_word:
        print('The {} letter is in the generated word!'.format(first_ask))

    elif second_ask  in generated_word:
        print('The {} letter is in the generated word!'.format(second_ask))

    elif third_ask  in generated_word:
        print('The {} letter is in the generated word!'.format(third_ask))

    elif fourth_ask  in generated_word:
        print('The {} letter is in the generated word!'.format(fourth_ask))



else:
    print("None of the letters are in the generated word!")       







            
