import random
from player import Player
from npc import generate_npc

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

    player = Player(name, strength, charisma, luck)
    return player

def tavern(player):
    while True:
        print("\nYou are in a noisy tavern in Tortuga.")
        print("What would you like to do?")
        print("1. Talk to a stranger")
        print("2. Play a game of dice")
        print("3. Check your stats")
        print("4. Leave game")

        choice = input("> ").strip()
        if choice == "1":
            talk_to_stranger(player)
        elif choice == "2":
            play_dice(player)
        elif choice == "3":
            player.show_stats()
        elif choice == "4":
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

def play_dice(player):
    print("\nYou sit down at a crooked table for a game of dice.")

    if player.gold <= 0:
        print("You have no gold to bet. The other pirates laugh at you as they shoo you away.")
        return

    print(f"You currently have {player.gold} gold.")
    bet_input = input("How much gold would you like to bet? ").strip()

    if not bet_input.isdigit():
        print("That is not a valid number.")
        return

    bet = int(bet_input)

    if bet <= 0:
        print("You must bet at least 1 gold.")
        return

    if bet > player.gold:
        print("You do not have enough gold to make that kind of bet.")
        return

    player_roll = random.randint(1, 6)
    house_roll = random.randint(1, 6)

    print(f"\nYou roll a {player_roll}.")
    print(f"Your opponent rolls a {house_roll}.")

    # Luck bonus:
    # luck 5 gives a bonus of 1
    # luck 6 gives a bonus of 2
    # luck 7 gives a bonus of 2
    player_total = player_roll + (player.luck // 3)

    if player_total > house_roll:
        print("You win the round!")
        player.gold += bet
    elif player_total < house_roll:
        print("You lose the round.")
        player.gold -= bet
    else:
        print("It's a tie. No gold changes hands.")

    print(f"You now have {player.gold} gold.")