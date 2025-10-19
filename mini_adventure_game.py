def treasure_room():
    print("You find a chest box ")
    print("The chest is heavy and old. Do you try to 'open' it, or 'leave' it and find a way out?")
    your_choice = input()
    if your_choice == "open":
        print( "You open the chest and find it full of gold! You WIN!")
    elif your_choice == "leave":
        print( "You leave the treasure behind and escape the room. You survived, but you'll always wonder what was inside.")
    else:
        print("You hesitate and a trap is sprung! GAME OVER.")
def locked_room():
    print("The door is locked, and you are stuck. GAME OVER.")
def start_game():
    print("You wake up in a dimly lit room. There is a wooden door to your 'left' and a steel door to your 'right' : ")
    while True:
        story = input("Enter either 'left' or 'right' " )
        if story == "left":
            treasure_room()
            break
        elif story == "right":
            locked_room()
            break
        else:
            print("Invalid choice")
start_game()