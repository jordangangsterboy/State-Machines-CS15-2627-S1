"""
Activity 6: State Machines
"""

import time


def traffic_light_state_machine():
    """
    Simple state machine: a traffic light.
    States: green -> yellow -> red -> green (repeats forever)
    Event: time passing (time.sleep)
    """
    state = "green"

    while True:
        if state == "green":
            print("GREEN LIGHT")
            time.sleep(5)
            state = "yellow"
        elif state == "yellow":
            print("YELLOW LIGHT")
            time.sleep(1)
            state = "red"
        elif state == "red":
            print("RED LIGHT")
            time.sleep(5)
            state = "green"


def coder_life_state_machine():
    """
    A more complex state machine that takes user input.
    States: coding, eating, sleeping
    Event: how the user says they're feeling
    Transitions (from the activity table):
        CODING   + tired  -> SLEEPING
        CODING   + hungry -> EATING
        CODING   + happy  -> CODING
        EATING   + full   -> CODING
        EATING   + hungry -> EATING
        EATING   + tired  -> SLEEPING
        SLEEPING + tired  -> SLEEPING
        SLEEPING + awake  -> CODING
        SLEEPING + hungry -> EATING
    """
    state = "coding"

    while True:
        if state == "coding":
            print("You are coding!")
            while True:
                feeling = input("How are you feeling? ").strip().lower()
                if feeling == "tired":
                    state = "sleeping"
                    break
                elif feeling == "hungry":
                    state = "eating"
                    break
                elif feeling == "happy":
                    state = "coding"
                    break
                else:
                    print("Not a valid event for this state. Try again.")

        elif state == "eating":
            print("You are eating!")
            while True:
                feeling = input("How are you feeling? ").strip().lower()
                if feeling == "hungry":
                    state = "eating"
                    break
                elif feeling == "full":
                    state = "coding"
                    break
                elif feeling == "tired":
                    state = "sleeping"
                    break
                else:
                    print("Not a valid event for this state. Try again.")

        elif state == "sleeping":
            print("You are sleeping!")
            while True:
                feeling = input("How are you feeling? ").strip().lower()
                if feeling == "hungry":
                    state = "eating"
                    break
                elif feeling == "awake":
                    state = "coding"
                    break
                elif feeling == "tired":
                    state = "sleeping"
                    break
                else:
                    print("Not a valid event for this state. Try again.")


def mood_state_machine():
    """
    Extension Activity: a mood state machine with 4 states.
    States: mad, sad, glad, bad
    Each state has at least 2 valid events that transition elsewhere.
    Invalid input does not change the state.

    Transitions:
        MAD  + calm_down -> GLAD
        MAD  + vent      -> SAD
        SAD  + cheer_up  -> GLAD
        SAD  + dwell     -> BAD
        GLAD + relax     -> GLAD
        GLAD + annoyed   -> MAD
        BAD  + rest      -> SAD
        BAD  + snap      -> MAD
    """
    state = "glad"

    while True:
        if state == "mad":
            print("You are MAD! Something ticked you off.")
            event = input("What do you do? (calm_down / vent) ").strip().lower()
            if event == "calm_down":
                state = "glad"
            elif event == "vent":
                state = "sad"
            else:
                print("Invalid event, try again.")

        elif state == "sad":
            print("You are SAD. Feeling down.")
            event = input("What do you do? (cheer_up / dwell) ").strip().lower()
            if event == "cheer_up":
                state = "glad"
            elif event == "dwell":
                state = "bad"
            else:
                print("Invalid event, try again.")

        elif state == "glad":
            print("You are GLAD! Life is good.")
            event = input("What do you do? (relax / annoyed) ").strip().lower()
            if event == "relax":
                state = "glad"
            elif event == "annoyed":
                state = "mad"
            else:
                print("Invalid event, try again.")

        elif state == "bad":
            print("You are having a BAD time. Everything feels off.")
            event = input("What do you do? (rest / snap) ").strip().lower()
            if event == "rest":
                state = "sad"
            elif event == "snap":
                state = "mad"
            else:
                print("Invalid event, try again.")


if __name__ == "__main__":
    # Uncomment ONE of these at a time to run that state machine.

    # traffic_light_state_machine()
    # coder_life_state_machine()
    mood_state_machine()
