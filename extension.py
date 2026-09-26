state = "chilling"

while True:
    if state == "chilling":
        print("You are chilling")
        feeling = input("How are you feeling? ").strip().lower()

        if feeling == "stressed":
            state = "stressing"
        elif feeling == "tired":
            state = "sleeping"
        elif feeling == "bored":
            state = "gaming"
        else:
            print("Invalid feeling, try again.")

    elif state == "stressing":
        print("You are stressing!")
        feeling = input("How are you feeling? ").strip().lower()

        if feeling == "stressed":
            state = "stressing"
        elif feeling == "tired":
            state = "sleeping"
        elif feeling == "bored":
            state = "gaming"
        else:
            print("Invalid feeling, try again.")

    elif state == "sleeping":
        print("You are sleeping!")
        feeling = input("How are you feeling? ").strip().lower()

        if feeling == "stressed":
            state = "stressing"
        elif feeling == "tired":
            state = "sleeping"
        elif feeling == "bored":
            state = "gaming"
        else:
            print("Invalid feeling, try again.")

    elif state == "gaming":
        print("You are gaming!")
        feeling = input("How are you feeling? ").strip().lower()

        if feeling == "stressed":
            state = "stressing"
        elif feeling == "tired":
            state = "sleeping"
        elif feeling == "bored":
            state = "gaming"
        else:
            print("Invalid feeling, try again.")