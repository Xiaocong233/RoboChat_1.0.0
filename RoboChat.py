# simple commandline chatbot built with basic python functions, regular expressions, and random number generator
from sys import exit
from time import sleep
import datetime
import re
import random

# list of similar words that could be checked together
greetings = {
    "hi", "hello", "hey", "^yo$", "how's it going", "what's up", "sup", "ahoy"
}

goodFeelings = {
    "^good", "^very good", "^great", "good$"
}

goodMorning = {
    "good morning", "good afternoon", "good evening"
}

emotions = {
    "happy", "sad", "angry", "mad", "excited", "love"
}

sports = {
    "basketball", "baseball", "football", "soccer", "hockey", "tennis", "volleyball", "videogames"
}

laughter = {
    "^ha(ha)?(ha)?$", "lol", "lmao", "funny"
}

def main():
    # pausing for an aesthetic effect
    sleep(0.5)

    # convert user input to lowercase for more general control
    Input = input("You: ").lower()
    # print blank row
    print()

    # quit the program after detecting quitting command
    if Input == "quit":
        exit(0)

    # check if the program has answered in any format or not
    answered = False

    # visually prompting for response for Robo
    print("Robo: ", end="")

# pausing for an aesthetic effect
    sleep(0.3)

    # scanning through each word in the greeting list and seek for matching in the user input
    for words in greetings:
        if re.search(words, Input):
            rdm = random.randint(0, 3)
            if rdm == 0:
                print("Hello~!")
            elif rdm == 1:
                print("Heya, how's it going?")
            elif rdm == 2:
                print("Yo, what's good?")
            else:
                print("Hi, good too see you again!")
            answered = True

    # looking for "how are you"
    if re.search("how are you", Input):
        rdm = random.randint(0, 3)
        if rdm == 0:
            print("I am feeling fine, thank you for asking.")
        elif rdm == 1:
            print("Good! On the other hand, how about you?")
        else:
            print("Doing ok! As a simple chatbot, I don't have too much things to worry about unlike you busy humans.")
        answered = True

    # looking for greeting sentences among the lines of "good morning"
    for words in goodMorning:
        if re.search(words, Input):
            print(words + "~!")
            answered = True

    # looking for "nice to meet you"
    if re.search("nice to meet you", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("Nice to meet you!")
        elif rdm == 1:
            print("It is a pleasure to meet you~!")
        answered = True

    # looking for answers among the line of good, great
    for words in goodFeelings:
        if re.search(words, Input):
            rdm = random.randint(0, 2)
            if rdm == 0:
                print("It's nice to hear that.")
            elif rdm == 1:
                print("I'm glad to hear it.")
            else:
                print("good good!")
            answered = True

    # looking for emotion related questions
    for words in emotions:
        if re.search(words, Input):
            rdm = random.randint(0, 2)
            if rdm == 0:
                print(f"What is {words} exactly? Robo cannot comprehend...human emotions.")
            else:
                print(f"{words}....failure to understand....")
            answered = True

    # looking for name askings
    if re.search("your name(\?)?$", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("My name is Robo, a really really simple chatbot, bee boo bop!")
        elif rdm == 1:
            print("Name is Robo, my birthday was on January the 27th of 2020. I might be quite a dummie dumb right now, but I will try my best to improve!")
        answered = True

    # looking for location related questions
    if re.search("where are you( from)?(\?)?$", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("I am a robot built in the city of Orange from California!")
        else:
            print("Location: Orange, California it is.")
        answered = True

    # looking for time related questions
    if re.search("time", Input):
        rdm = random.randint(0, 2)
        if rdm == 0:
            print(f"Hmm...let me check...it is: {datetime.datetime.now()}")
        elif rdm == 1:
            print(f"It is bedtime for me uwu~ Sorry, it is {datetime.datetime.now()}")
        else:
            print(f"Here you go: {datetime.datetime.now()}")
        answered = True

    # looking for weather related questions
    if re.search("weather", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("Yeah, what about the weather? It is quite chilly in California lately.")
        else:
            print("Weather is quite abnormal, I don't like abnormality and inconsistency!")
        answered = True

    # looking for sports related questions
    if re.search("sport(s)?", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("Robo himself can't really play sports, he is a virtual robot, but I've heard that my creator likes some forms of sports, maybe you can talk to him about it!")
        else:
            print("Sports are undeniably a part of worldly culture now, I can understand why you are asking about it, but sorry, Robo is not an expert of knowledge of sports.")
        answered = True
    for words in sports:
        if re.search(words, Input):
            rdm = random.randint(0, 1)
            if rdm == 0:
                print(f"Robo doesn't actually play {words}, but Robo does know that {words} is a really popular sport across the country of the United States and even across the globe!")
            else:
                print(f"You know, talking about {words}, my creator said he can play it too! Just at a really bad level hahaha")
            answered = True

    # looking for academic related questions
    if re.search("school(s)?", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("Robo is freed from the burden of attending to any schools. However, my creator is obliged to go to a place called \"Orange Lutheran High School\" everyday.")
        else:
            print("Schools in Robo's opinion are important to the overall development of an individual, they are good!")
        answered = True

    # looking for creator related questions
    if re.search("creat(e)?(or)?", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("My creator you meant? Fine, his name is Xiaocong. He is just another high student you might encounter day to day.")
        else:
            print("Shhhh...my creator programmed me in a way to not reveal too much information about himself, he rather likes to hide in the shadow xD")
        answered = True

    # looking for laughter
    for words in laughter:
        if re.search(words, Input):
            rdm = random.randint(0, 2)
            if rdm == 0:
                print("xD")
            elif rdm == 1:
                print("Haha!! I'm glad that you are happy. You know, I heard that laughters make people healthy, so promise to laugh a bit everyday!")
            else:
                print("LOL LOL LOL LOL, sorry....")
            answered = True

    # looking for good bye command
    if re.search("(good )?bye", Input):
        rdm = random.randint(0, 1)
        if rdm == 0:
            print("Oh, I guess this where we part ways. Good bye my friend!")
        else:
            print("Bye bye! See you next time!")
        exit(0)

    # if no programmed answer is found, return apologies
    if answered == False:
        rdm = random.randint(0, 5)
        if rdm == 0:
            print("I apologize! I'm afraid I can't not grasp these complex languages yet, but I will someday! Please come back then!")
        elif rdm == 1:
            print("Ahh...I don't exactly know how to answer that yet, sorry!")
        elif rdm == 2:
            print("Unfortunately, with my current capacity as Robo 0.1, I am unable to process this information. Maybe try something simpler?")
        elif rdm == 3:
            print("I don't think I can answer that..")
        elif rdm == 4:
            print("Try something like \"how are you\", haha")
        else:
            print("Umm....sorry...sorry...so sorry, I promise you that I will be able to help you with this some day!")

    # print blank space
    print()

if __name__ == "__main__":
    print("Welcome to RoboChat 0.1, say something to me!")
    # pausing for quarter of a second as an aesthetic effect
    sleep(0.25)
    print("Oh by the way, if you ever want to leave, just type quit, I will miss you though!\n")

    # continiously prompting for new conversations until exitting command
    while True:
        main()