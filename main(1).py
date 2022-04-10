import time
import random

drama = input("Before we begin, would you like to have a more dramatic storytelling\n"
              "experience, with each line appearing one at a time? (y/n:) ")
if drama == "y":
    def dramatic_presentation(str):
        for i in str:
            if i == "`":
                time.sleep(1)
            else:
                print(i, end="")
                if i == "." or i == ",":
                    time.sleep(0.5)
                time.sleep(0.02)
else:
    def dramatic_presentation(str):
        print(str)

time.sleep(0.5)
pre_opening = "Thank you. Beginning the story...\n\n"

dramatic_presentation(pre_opening)

time.sleep(1)

opening = "It's the day of the hackathon. And you're screwed.`\n" \
          "You've always been interested in coding. You got a coding book a while\n" \
          "ago, and have been slowly chipping away at it when you had the time.`\n" \
          "When you heard about the Ridge hackathon and the workshops it offered,\n" \
          "you decided to sign up. Why not? There was plenty for you to do, and a\n" \
          "competition that you could attempt a submission in. \n\n" \
          "`You decided to bring only a couple things to the hackathon. You don't\n" \
          "want to weigh yourself down with too much, anyway.\n" \
          "`You had a decent assortment of options to choose from:\n\n" \
          "`1. A laptop. It's still in its pristine 2013 shine.\n" \
          "`2. Your coding book. It's heavier than your industrial laptop.\n" \
          "`3. A 2 liter water bottle. It'll last the whole day if filled.\n" \
          "`4. Earbuds. Coding's much less fun without them.\n" \
          "`5. Your pet bird. It probably knows as much about coding as you do.\n" \
          "`6. A toothbrush. Dental hygiene is always your top priority.\n" \
          "`7. A Color of My Love CD and a portable CD player. For obvious reasons.\n" \
          "`8. Sunglasses. It's important to look as cool as possible while coding.\n" \
          "`9. A clock. Everyone will surely be impressed by your timekeeping service.\n" \
          "`10. A mouse. You've trained it to be able to sneak off and deliver you information.\n\n" \

dramatic_presentation(opening)

inventory = []
choices = {'1': 'Naturally. Your laptop slotted neatly into your backpack.',
           '2': 'Of course. The hefty book got placed at the base of your backpack.',
           '3': 'Precisely. You filled up the bottle and slid it in.',
           '4': 'Certainly. You slid the buds into your pocket.',
           '5': "By all means. You placed it into it's travel cage.",
           '6': 'Indeed. You put the brush and some toothpaste in a bag.',
           '7': 'But of course. You patted them lovingly after putting them into your backpack.',
           '8': 'Undestandable. You put them on immediately.',
           '9': 'Surely. You taped it onto your chest, and another onto your back.',
           '10': 'Indubitably. You gave it a treat and slipped it into your pocket.'}

choice_obj = {'1': 'Laptop',
           '2': 'Coding book',
           '3': 'Water bottle',
           '4': 'Earbuds',
           '5': "Bird",
           '6': 'Toiletries',
           '7': 'CD',
           '8': 'Sunglasses',
           '9': 'Clock',
           '10': 'Rodent'}

choice = 0
try:
    choice = int(input("What did you want to pack first? (enter an integer:) "))
except:
    print("Please enter an integer.")

def choice_handling(choice):
    inventory.append(choice_obj[str(choice)])
    desc_choice = choices[str(choice)]
    dramatic_presentation(desc_choice + "\n")
    del choices[str(choice)]

choice_handling(choice)

print(choices)
key_item = False

if choice == 1 or choice == 2:
    disclaimer = ''
    key_item = True
    if choice == 1:
        del choices['2']
        disclaimer = "Because you packed your large laptop, you cannot bring your coding book.\n"
    elif choice == 2:
        del choices['1']
        disclaimer = "Because you packed your large coding book, you cannot bring your laptop.\n"
    dramatic_presentation(disclaimer)

try:
    choice = int(input("What did you want to pack next? (enter an integer:) "))
except:
    print("Please enter an integer.")

choice_handling(choice)

# Force to choose key item if not already

if "Laptop" not in inventory and "Coding book" not in inventory:
    while key_item == False:
        try:
            choice = int(input(
                "You must bring your laptop or coding book,\n"
                "but you only have room for one more item.\n"
                "What did you bring? (enter 1 or 2:) "))
            if choice == 1 or choice == 2:
                key_item = True
            else:
                dramatic_presentation("Comedy gold...")
        except:
            print("Please enter an integer.")

else:
    try:
        choice = int(input("You had space for one more item. What was it? (enter an integer:) "))
    except:
        print("Please enter an integer.")

choice_handling(choice)

dramatic_presentation("With your bag thoughtfully packed, you sped off to\n"
                      "the site of the hackathon in a breezy jog.\n"
                      "`You approached the high school from the elementary school,\n"
                      "but a group of elementary schoolers had already claimed\n"
                      "the territory for themselves. They sensed your presence\n"
                      "and approach. You were cornered from all directions.\n"
                      "`They challenged you to a game of hangman. There was\n"
                      "no getting around this...\n\n")

word = ""
lives = 5
no_quit = True

dramatic_presentation("...Welcome to hangman!")

while no_quit:

    selection = ["window", "rhythm", "luxury", "beekeeper", "jukebox",
                 "fixable", "ready and willing", "calm and collected",
                 "ridge hacks", "try and guess", "destruction", "april showers"]
    word = random.choice(selection)
    selection.remove(word)

    guess_status = ""
    guess_str_status = ""
    word_list = []

    for i in word:
        if i == " ":
            guess_status += " "
        else:
            guess_status += "-"
        word_list.append(i)

    print(guess_status)

    previous_guesses = []
    null_lose = False
    while guess_str_status != word and lives != 0:
        time.sleep(1)
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if guess in previous_guesses:
            print("You already guessed that!")
            time.sleep(1)
            null_lose = True
        previous_guesses.append(guess)
        guess_status = []

        for x in word_list:
            if x == guess:
                guess_status.append(guess)
            elif x == " ":
                guess_status.append(" ")
            else:
                if x in previous_guesses:
                    guess_status.append(x)
                else:
                    guess_status.append("-")

        if guess in word_list or null_lose:
            pass
        else:
            lives -= 1

        guess_str_status = ""
        for i in guess_status:
            guess_str_status += i

        dramatic_presentation(guess_str_status)
        dramatic_presentation(f"Lives: {lives}")
        dramatic_presentation(f"Previous guesses: {previous_guesses}\n")

    if guess_str_status == word:
        yes = input("You guessed the word! Play again? (y/n:) ")
    else:
        yes = input("The children taunt your failure. Play again?")
    if yes == "n":
        no_quit = False

status = ""

dramatic_presentation("The children had been satisfied, and left you alone.\n"
                      "`Your emotional stability had been wounded, and you\n"
                      "needed to fix it, fast. You could:\n"
                      "`1. Use an item. (The item might be used up.)\n"
                      "`2. Play in the fields. (You will suffer exhaustion.)\n")

try:
    choice2 = int(input("What did you do? (enter 1 or 2): "))
    if choice2 == 1:
        dramatic_presentation(f"Your inventory was: {inventory}")
        choice3 = input(
            "What item did you use? (write the full, capitalized name of the item:) ")
        choice_descr = {
            'Water bottle': 'You chugged the water, overcome with thirst.\n'
                            'You were left with a half-empty bottle.',
            'Earbuds': 'You rolled the earbuds between your fingers, since there\n'
                       'was nothing to connect them to.',
            "Bird": "You watched as your bird flew around for a while. 'Your bird\n"
                    "returned, with a leaf. It didn't get added to your inventory.",
            'Toiletries': 'You brushed your teeth without water. It felt amazing.',
            'CD': 'You listened to the voice of your generation.',
            'Sunglasses': 'You put the glasses over your eyes and acted tough.',
            'Clock': "You checked the time. You felt relieved.",
            'Rodent': "You played with your mouse. Your mouse looked happy."}

        while choice3 == 'Laptop' or choice3 == 'Coding book':
            if choice3 == 'Laptop' or choice3 == 'Coding book':
                dramatic_presentation("You need to save it for later.")
                choice3 = input(
                    "What item did you use? (write the full, capitalized name of the item:) ")
        dramatic_presentation(choice_descr[choice3])
        if choice3 == "Water bottle":
            inventory.remove('Water bottle')
            inventory.append('Half-empty water bottle')
    elif choice2 == 2:
        status = "Tired"
        dramatic_presentation(
            "You frolicked in the fields. Reconnecting with nature\n"
            "was healing. You look across the field, taking in\n"
            "the natural beauty of things. You climb trees and make friends\n"
            "with the birds. You play poker with the squirrels. You\n"
            "run with the deer. You are free... but tired.\n\n")
except:
    print("Please enter an integer.")

if status == 'Tired':
    dramatic_presentation("You trudged into the school building.")
else:
    dramatic_presentation("You walked into the school building.")
dramatic_presentation("You then took a t-shirt,\n"
                          "a sticker, and attended the opening ceremony. There, you\n"
                          "began to think about the project you would begin.\n"
                          "Breakfast came and went, and you charged yourself up\n"
                          "with some caffine. `Ready to begin, you settled yourself\n"
                          "into a booth in the cafeteria. Looking across the room, you saw\n"
                          "that an unspecified, completely ambiguous group\n"
                          "had already finished their tic-tac-toe logic game,\n"
                          "and was in the process of connecting it up to\n"
                          "a strange, laser-producing device. You decided to give\n"
                          "it a try...")

import random

game = "no"
row1 = "---"
row2 = "---"
row3 = "---"
list1 = ["-", "-", "-"]
list2 = ["-", "-", "-"]
list3 = ["-", "-", "-"]
unmoved = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print(f"{row1}\n{row2}\n{row3}")
print(
    "Welcome to TicTacToe! Using the grid, 1 - 9 (the same format as your number pad!), try to get three of your symbol, x, diagonal, vertical, or horizontal across the board")

grid = []

while game != "won":
    action = input("Where do you want to go? ")
    if action == "1":
        grid.append("1")
        list3[0] = "X"
    if action == "2":
        grid.append("2")
        list3[1] = "X"
    if action == "3":
        grid.append("3")
        list3[2] = "X"
    if action == "4":
        grid.append("4")
        list2[0] = "X"
    if action == "5":
        grid.append("5")
        list2[1] = "X"
    if action == "6":
        grid.append("6")
        list2[2] = "X"
    if action == "7":
        grid.append("7")
        list1[0] = "X"
    if action == "8":
        grid.append("8")
        list1[1] = "X"
    if action == "9":
        grid.append("9")
        list1[2] = "X"

    unmoved.remove(action)

    print(f"{list1}\n{list2}\n{list3}")

    ai_move = random.choice(unmoved)

    if ai_move == "1":
        grid.append("1")
        list3[0] = "O"
    if ai_move == "2":
        grid.append("2")
        list3[1] = "O"
    if ai_move == "3":
        grid.append("3")
        list3[2] = "O"
    if ai_move == "4":
        grid.append("4")
        list2[0] = "O"
    if ai_move == "5":
        grid.append("5")
        list2[1] = "O"
    if ai_move == "6":
        grid.append("6")
        list2[2] = "O"
    if ai_move == "7":
        grid.append("7")
        list1[0] = "O"
    if ai_move == "8":
        grid.append("8")
        list1[1] = "O"
    if ai_move == "9":
        grid.append("9")
        list1[2] = "O"
    unmoved.remove(ai_move)
    print(f"{list1}\n{list2}\n{list3}")
    game = "won"

if "Laptop" not in inventory:
    dramatic_presentation("You realized that you still needed a computer in order\n"
                          " to write your code, and luckily find an empty space\n"
                          "in the media center. Arming yourself with limitless\n"
                          "knowledge, you soon lose yourself to the infinite\n"
                          "silence of the center.\n`Time began to melt into itself.\n"
                          "All you could see was the coding in front of you.\n"
                          "It was a terrifying, raw, and real moment of time.\n")
dramatic_presentation("You had to admit that the logic of their project worked\n"
                      "as expected, and the finished product would be incredible.\n"
                      "But you didn't dawdle on that for long, and began to work.\n"
                      "`Time began to melt into itself. The cafeteria's constant\n"
                      "songs began to blend in your mind, and all you could really\n"
                      "see was the coding in front of you. It was a terrifying,\n"
                      "raw, and real amount of time. And you suddenly realized\n"
                      "that your coding didn't even make much sense, much less work...\n")

dramatic_presentation("'TO\n'BE\n'CONTINUED")