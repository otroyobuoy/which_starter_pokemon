# which starter pokemon should you choose in scarlet/violet quiz

import random


# custom functions

def which_pokemon(letter):
    """ match answer to pokemon """
    if letter == answers_copy[0]:
        return "Sprigatito"
    elif letter == answers_copy[1]:
        return "Quaxly"
    elif letter == answers_copy[2]:
        return "Fuecoco"
    if letter == answers_copy[3]:
        return "Sprigatito"
    elif letter == answers_copy[4]:
        return "Quaxly"
    elif letter == answers_copy[5]:
        return "Fuecoco"


# keeping track of the answers

pokemon_names = {"Sprigatito": 0,
                 "Quaxly": 0,
                 "Fuecoco": 0}

# title
print("--- Which Starter Pokémon Should You Choose in Scarlet/Violet Quiz ---\n")

# a dictionary of questions and, their answers in order
questions = {
    "What's your favourite dessert?\n":
        ["Apple Pie", "Fruit Salad", "Chocolate Cake",
         "Ice Cream Sundae", "Bobba Tea", "MORE DINNER"],
    "What is your ideal date?\n":
        ["Make something cute together", "Have a picnic", "Hit the arcade",
         "April 25th", "Go for a hike", "Make a fort and watch movies"],
    "How would your friends describe you?\n":
        ["Confident and generous", "Introverted and thoughtful", "Loyal and reliable",
         "Chaotic and enthusiastic", "Organised and considerate", "Laid back and easy to be around."],
    "What are you likely to be doing at a party?\n":
        ["Playing truth or dare", "Organising a board game to play", "Snacking in the kitchen",
         "Doing karaoke", "Finding a quiet place", "Chatting with your friends on the couch"],
    "How would you like to spend a night alone?\n":
        ["Getting crafty", "Getting stuff organised infront of the TV", "Playing video games",
         "Getting dressed up and taking pics", "Baking", "Catching up on some zzzzz"],
    "What's your favourite holiday?\n":
        ["Halloween", "Valientine's Day", "Matariki",
         "New Years Eve", "Christmas", "Hiberna"],
    "What's your favourite season?\n":
        ["Summer", "Spring", "Winter", "Pride", "Awards", "Basketball"],
    "Which word best describes your fashion sense?\n":
        ["Colourful and chaotic", "Cute but practical", "Casual, I just like to be comfy",
         "Lots of patterns and accessories", "Timeless and chic", "Shirt and jeans every day!", ]
}

# randomising the order of answers

for question, answers in questions.items():
    answers_copy = answers.copy()
    a = answers.pop(random.randint(0, 5))
    b = answers.pop(random.randint(0, 4))
    c = answers.pop(random.randint(0, 3))
    d = answers.pop(random.randint(0, 2))
    e = answers.pop(random.randint(0, 1))
    f = answers.pop()

    # asking multiple choice question
    print(f"\n{question}")
    answer = input(f"a) {a}\nb) {b}\nc) {c}\nd) {d}\ne) {e}\nf) {f}\n")

    # checking the answer input is valid
    while answer not in ["a", "b", "c", "d", "e", "f"]:
        print("Sorry, that is not a valid answer value, please try again.")
        answer = input()

    # figuring out which pokemon that answer aligns with using the custom fuction
    # and adding to the count for that pokemon
    if answer == "a":
        pokemon = which_pokemon(a)
        pokemon_names[pokemon] += 2
    elif answer == "b":
        pokemon = which_pokemon(b)
        pokemon_names[pokemon] += 2
    elif answer == "c":
        pokemon = which_pokemon(c)
        pokemon_names[pokemon] += 2

    elif answer == "d":
        pokemon = which_pokemon(d)
        pokemon_names[pokemon] += 1
    elif answer == "e":
        pokemon = which_pokemon(e)
        pokemon_names[pokemon] += 1
    elif answer == "f":
        pokemon = which_pokemon(f)
        pokemon_names[pokemon] += 1

# seeing which pokemon has the highest number of aligned answers
your_starter = (max(pokemon_names, key=pokemon_names.get))

# revealing the answer!
print(f"\nYou should choose {your_starter} to be your buddy Pokémon!")
