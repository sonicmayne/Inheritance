# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define povname = ""
define g = Character("")
define pov = Character("[povname]")

# The game starts here.

label start:
    g "Nonogram?"
    menu:
        "Yes":
            jump play_nonogram
        "No":
            pass

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "You"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    pov "My name is [povname]"
    g "Are you over 18?"
    menu:
        "yes":
            g "Let the fun begin!"
        "no":
            g "Alas, you are too young to read the exciting story contained within this game..."
            return

    g "Hello player. Text will go here. And here."
    g "Weeb detected! Weeb detected!"
    jump play_nonogram

    # This ends the game.

    return
