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


if __name__ == "__main__":
    # Uncomment ONE of these at a time to run that state machine.

    # traffic_light_state_machine()
    coder_life_state_machine()