class Location:
    def __init__(self, name, location_type, description):
        self.name = name
        self.location_type = location_type
        self.description = description
        self.npcs = []
        self.connected_locations = []

    def describe(self):
        print(f"\n=== {self.name} ===")
        print(f"Type: {self.location_type}")
        print(self.description)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def add_connection(self, location):
        self.connected_locations.append(location)