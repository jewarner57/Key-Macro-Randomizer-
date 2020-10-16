from pyautogui import press, hotkey
import time
from random import choice, randint

KeyMacroGroupList = [
(
    # Chewbacca Normal
    # Key1,   Key2,  Key3, Time Delay
    ("ctrl", "shift", "1", 1),
    ("ctrl", "shift", "2", 1.1),
    ("ctrl", "shift", "3", 1.1),
),
(
    # Chewbacca Angry
    # Key1,   Key2,  Key3, Time Delay
    ("ctrl", "alt", "1", 1),
    ("ctrl", "alt", "2", 1.1),
    ("ctrl", "alt", "3", 1.6),
),
(
    # Chewbacca Sad
    # Key1,   Key2,  Key3, Time Delay
    ("ctrl", "fn", "1", 1),
    ("ctrl", "fn", "2", 1.1),
    ("ctrl", "fn", "3", 1.1),
),

]

def chooseRandomCombo(macroList, repeatAmount, noRepeat):
    """Triggers a random item from the macros array """
    prevMacro = "" 
    for _ in range(1, repeatAmount+1):
        # choose a random item from the macro list
        macro = choice(macroList)

        # pick again if the macro is the same as the previous one
        while macro == prevMacro and noRepeat:
            macro = choice(macroList)

        prevMacro = macro

        hotkey(macro[0], macro[1], macro[2])
        time.sleep(macro[3])

endProgram = False
while endProgram == False:
    try:

        print("\nPress Control-C to quit or enter 0.\n")
        userInput = ""
        while not userInput.isnumeric():
            userInput = input("Choose A Macro List. Enter: 1 or 2 or 3\n")

        if int(userInput) == 0:
            endProgram = True
            break
        
        macroList = [*KeyMacroGroupList[int(userInput)-1]]
        chooseRandomCombo(macroList, 5, True)

    except KeyboardInterrupt:
        endProgram = True


