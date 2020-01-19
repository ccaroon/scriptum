import adventurelib

class Room(adventurelib.Room):
    # items   - Items in the room that can be picked up.
    # objects - Items in the room that are stationary but can be interacted with:
    #           I.e. doors, windows, floor, carpet, large paintings, etc.
    # NESW    - Exit to another room in that direction.
    def __init__(self, name, desc, items=[], objects=[], north=None, east=None, south=None, west=None):
        super().__init__(desc)
        self.name = name

        self.items = adventurelib.Bag()
        for item in items:
            self.items.add(item)

        self.objects = adventurelib.Bag()
        for obj in objects:
            self.objects.add(obj)

        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def __str__(self):
        return F"--- {self.name} ---\n{self.description}"
