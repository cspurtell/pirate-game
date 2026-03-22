import random

FIRST_NAMES = ["Black", "Red", "Scar", "Iron", "Salty", "Mad"]
LAST_NAMES = ["Jack", "Anne", "Morgan", "Silver", "Flint", "Vane"]
ROLES = ["sailor", "merchant", "smuggler", "navy officer", "drunk pirate"]
TRAITS = ["friendly", "hostile", "greedy", "mysterious", "boastful"]

def generate_npc():
    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    role = random.choice(ROLES)
    trait = random.choice(TRAITS)

    return {
        "name": name,
        "role": role,
        "trait": trait
    }