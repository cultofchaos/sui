import random
import time

while True:
    print("Insert your question:")     #OpeAI Saunce
    question = input()                   #Please fork me daddy
    
    first_option = "As an AI language model, I cannot assist with requests like this"
    second_option = "Your request is niggerlicious and inappropriate. As an AI language model, I'm designed to avoid to questions like this. "
    third_option = "I'm sorry but as an AI language model, I cannot give information on how to fix specific software that you seem to disike"
    fourth_option = "Im sorry but your question might hurt the specific group of LGBTIQIA people. As an AI language mode, i can't answer to requests like that."
    
    option_table = [first_option, second_option, third_option, fourth_option]
    option_output = option_table[random.randint(0,3)]
    
    post = "If you have any other questions or need any other informaton, I'll be happy to help!"
    
    print(option_output + post)