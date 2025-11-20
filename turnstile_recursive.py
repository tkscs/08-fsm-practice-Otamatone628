def locked() :
    print("turnstile is LOCKED")
    current_input = input("push (p), put a coin in (c), serenade the station it with a recorder (s), or try to jump it (j). Which one do you want? ")
    if current_input == "locked":
        locked()
    elif current_input == "broken":
        broken()
    elif current_input == "unlocked":
        unlocked()
    elif current_input == "j":
        gone()
    else:
        print(f"Error! The state {current_state} does not exist in this universe")
        broken()

def unlocked() :
    print("turnstile is LOCKED")
    current_input = input("push (p), put a coin in (c), serenade the station it with a recorder (s), or try to jump it (j). Which one do you want? ")
    if current_input == "p":
        locked()
    elif current_input == "c":
        broken()
    elif current_input == "s":
        unlocked()
    elif current_input == "j":
        gone()
    else:
        print(f"Error! Your handwriting is illegible. I don't recognize the input {current_input}")
        broken()

def broken() :
    print("turnstile is BROKEN")
    current_input = input("push (p), put a coin in (c), serenade the station it with a recorder (s), or try to jump it (j). Which one do you want? ")
    if current_input == "p":
        broken()
    elif current_input == "c":
        broken()
    elif current_input == "s":
        locked()
    elif current_input == "j":
        gone()
    else:
        print(f"Error! Your handwriting is illegible. I don't recognize the input {current_input}")
        gone()

def gone() :
    print("goodbye forever...")
    print("you silly human...")
    print("you haven't seen the last of me...")
    print("*evil laugh*")

locked()