class Player:
    def __init__(self, name, strength, charisma, luck):
        self.name = name
        self.strength = strength
        self.charisma = charisma
        self.luck = luck
        self.gold = 10
        self.reputation = 0
        self.missing_eye = False
        self.missing_hand = False

    def show_stats(self):
        print("\n=== Captain Stats ===")
        print(f"Name: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Charisma: {self.charisma}")
        print(f"Luck: {self.luck}")
        print(f"Gold: {self.gold}")
        print(f"Reputation: {self.reputation}")
        print(f"Missing eye: {self.missing_eye}")
        print(f"Missing hand: {self.missing_hand}")
        print("=====================\n")