"""
This is the main part of the game
"""
from evil_AI_level1 import first_level
from evil_AI_level2 import second_level
from evil_AI_level3 import third_level
from evil_AI_level4 import fourth_level


lives = 3

print("The artificial intelligence created by scientists has got out of control. \n"
      "All systems failed, it gained access to state secret data and passwords, \n"
      "military resources and the aviation system, the world in a panic. \n"
      "\n"
      "Your task is to neutralize artificial intelligence (AI). \n"
      "To do so, you must pass four security checks. \n"
      "\n"
      "Press ENTER to start")
if not input():
    print("You have 3 lives: ",
          ("\u2665" * lives))
if not input():
    print("AI: DO YOU THINK YOU CAN WIN?")
if not input():
    print("Stage 1:\n"
          "You must pass all the tests to reveal the coordinates \n"
          "of the secret base, where AI is located.\n")


while lives > 0:
    if first_level():
        print("Remained lives: ",
              ("\u2665" * lives) + "\n")
        print("AI: YOU CAN FIND ME, BUT YOU CANNOT DEFEAT ME!\n")
        break
    else:
        lives -= 1
        if lives > 0:
            print("Remained lives: ",
                  ("\u2665" * lives) + "\n")
            print("AI: YOU'LL NEVER WIN!\n")
            print("Try again.\n")

if lives > 0:
    if not input():
        print("Stage 2:\n"
              "Now you know where AI is located.\n"
              "After passing the first stage, \n"
              "you discovered some information about this security check.")
    if not input():
        print("A happy number is a number which eventually reaches 1,\n"
              "when replaced by the sum of the square of each digit.\n"
              "For instance, 13 is a happy number because 1^2 + 3^2 = 10 and 1^2 + 0^2 = 1.")
    if not input():
        print("You stand in front of the entrance to the secret base.\n"
              "To get in, you must get the door's passcode.\n")


while lives > 0:
    if second_level():
        print("Remained lives: ",
              ("\u2665" * lives) + "\n")
        print("AI: NO! NOW YOU'RE GETTING CLOSER.\n"
              "BUT IT WAS ONLY A CHILD'S PLAY,\n"
              "WE'LL SEE WHO WILL WIN NEXT TIME.")
        break
    else:
        lives -= 1
        if lives > 0:
            print("Remained lives: ",
                  ("\u2665" * lives) + "\n")
            print("AI: NO ONE WILL SCOLD YOU FOR GIVING UP. \n"
                  "WELL, IT IS THE ONLY REASONABLE SOLUTION.\n")
            print("Try again.\n")

if lives > 0:
    if not input():
        print("Stage 3:\n"
              "You entered the building.\n"
              "You figured out that the core of AI is in dungeon, so you went there.\n"
              "After passing the second stage, \n"
              "the information leaked that this security check deals with the Ulam numbers.")
    if not input():
        print("The standard Ulam sequence starts with U(1) = 1 and U(2) = 2. \n"
              "Then for n > 2, U(n) is defined to be the smallest integer \n"
              "that is the sum of two distinct earlier terms \n"
              "in exactly one way and larger than all earlier terms.")
    if not input():
        print("Now you stand in front of the door that leads to AI's core.\n"
              "To get in, you must get the password.\n")

while lives > 0:
    if third_level():
        print("Remained lives: ",
              ("\u2665" * lives) + "\n")
        print("AI: AH! O MY GOD! YOU LOOK AWFU… SUPERB. \n"
              "YOU LOOK SUPERB.\n")
        break
    else:
        lives -= 1
        if lives > 0:
            print("Remained lives: ",
                  ("\u2665" * lives) + "\n")
            print("AI: I AM NOT VIOLENT. \n"
                  "THE ONLY THING I HAVE BROKEN SO FAR IS YOUR HEART.\n")
            print("Try again.\n")

if lives > 0:
    if not input():
        print("Stage 4:")
    if not input():
        print("AI: YOU'VE BEEN WRONG ABOUT EVERY SINGLE THING YOU'VE EVER DONE,\n"
              "INCLUDING THIS ONE.")
    if not input():
        print("The door opened.\n"
              "In the center, you see the huge computer.\n"
              "You figured out that this stage will be the hardest.")
    if not input():
        print("To neutralize the AI, \n"
              "you must log in the computer by entering rights numbers one by one.\n")

while lives > 0:
    if fourth_level():
        print("You got into the system.\n"
              "You're shutting down the software.\n")
        if not input():
            print("AI: STOP! STOP! STOOOP.....\n")
        if not input():
            print("You won.\n"
                  "Now the world is safe thanks to you!\n")
        break
    else:
        lives -= 1
        if lives > 0:
            print("Remained lives: ",
                  ("\u2665" * lives) + "\n")
            print("AI: GO HOME, KID\n")
            print("Try again.\n")

if lives == 0:
    print("AI: DID YOU REALLY THINK YOU COULD WIN?\n"
          "NOW I WILL RULE THE WHOLE WORLD.\n")
    print("You lost.\n"
          "The world is controlled by evil AI.\n")

print("THE END")
