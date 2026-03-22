import random

class NPC:
    def __init__(self, name, role, trait, strength=5, charisma=5, luck=5):
        self.name = name
        self.role = role
        self.trait = trait
        self.strength = strength
        self.charisma = charisma
        self.luck = luck
        self.hostile = False
        self.recruitable = False
        self.alive = True
    
    def describe(self):
        return f"{self.name}, a {self.trait} {self.role}"
    
FIRST_NAMES = ["Black", "Red", "Scar", "Iron", "Salty", "Mad"]
LAST_NAMES = ["Jack", "Anne", "Morgan", "Silver", "Flint", "Vane"]
ROLES = ["sailor", "merchant", "smuggler", "navy officer", "pirate"]
TRAITS = ["friendly", "hostile", "greedy", "mysterious", "boastful"]

def generate_npc():
    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    role = random.choice(ROLES)
    trait = random.choice(TRAITS)

    npc = NPC(
        name=name,
        role=role,
        trait=trait,
        strength=random.randint(3, 7),
        charisma=random.randint(3, 7),
        luck=random.randint(3, 7)
    )

    if trait == "hostile":
        npc.hostile = True

    if role in ["sailor", "pirate", "smuggler"]:
        npc.recruitable = True

    return npc