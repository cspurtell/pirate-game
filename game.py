from player import Player

def create_player():
    print("Welcome to Pirate Game!")
    name = input("What shall your captain's name be? ").strip()

    if not name:
        name = "Unnamed Captain"

    print("Choose your speciality:")
    print("1. I want to be strong")
    print("2. I want to be charming")
    print("3. I want to be lucky")

    choice = input("> ").strip()

    strength = 5
    charisma = 5
    luck = 5

    if choice == "1":
        strength += 2
    elif choice == "2":
        charisma += 2
    elif choice == "3":
        luck += 2
    else:
        print("No specialty chosen. You are average in all things.")

def tavern(player):
    while True:
        print("\nYou are in a noisy tavern in Tortuga.")
        print("What would you like to do?")
        print("1. Talk to a stranger")
        print("2. Check your stats")
        print("3. Leave game")

        choice = input("> ").strip()

        if choice == "1":
            talk_to_stranger(player)
        elif choice == "2":
            player.show_stats()
        elif choice == "3":
            print(f"Farewell, Captain {player.name}.")
            break
        else:
            print("Invalid choice. Try again.")

def talk_to_stranger(player):
    print("\nA rough-looking sailor squints at you.")

    if player.charisma >= 7:
        print("You charm the sailor with ease.")
        print("He buys you a drink and shares a rumor.")
        player.gold += 2
        player.reputation += 1
    else:
        print("The sailor laughs at your awkward attempt at conversation.")
        print("You gain nothing but embarrassment.")