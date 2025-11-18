# write code to implement a turnstile

# states

# inputs

# transitions

# starting state

# ending states

# possible states are: locked, unlocked, broken, gone
current_state = "locked"

# every time through the loop, we...
# get a new input
# transition to the next state

while current_state != "gone":

    # Experience being in the state that we're in
    if current_state == "locked":
        print("turnstile is LOCKED")
    elif current_state == "broken":
        print("turnstile is BROKEN")
    elif current_state == "unlocked":
        print("turnstile is UNLOCKED")
    else:
        print(f"Error! The state {current_state} does not exist in this universe")
        

    # get the input
    current_input = input("push (p), put a coin in (c), serenade the station it with a recorder (s), or try to jump it (j). Which one do you want? ")

    # transition to the next state based on the current state and the input
    if current_state == "locked":
        # handle each input
        if current_input == "p":
            current_state = "broken"
        elif current_input == "c":
            current_state = "unlocked"
        elif current_input == "s":
            current_state = "locked"
        elif current_input == "j":
            current_state = "gone"
        else:
            print(f"Error! Your handwriting is illegible. I don't recognize the input {current_input}")
    elif current_state == "unlocked":
        # handle each input
        if current_input == "p":
            current_state = "locked"
        elif current_input == "c":
            current_state = "broken"
        elif current_input == "s":
            current_state = "unlocked"
        elif current_input == "j":
            current_state = "gone"
        else:
            print(f"Error! Your handwriting is illegible. I don't recognize the input {current_input}")
    elif current_state == "broken":
        # handle each input
        if current_input == "p":
            current_state = "broken"
        elif current_input == "c":
            current_state = "broken"
        elif current_input == "s":
            current_state = "locked"
        elif current_input == "j":
            current_state == "gone"
        else:
            print(f"Error! Your handwriting is illegible. I don't recognize the input {current_input}")
    elif current_state == "gone":
        break
    else:
        print(f"Error! You are in a simulation where the state {current_state} does not exist")