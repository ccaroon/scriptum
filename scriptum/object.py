from adventurelib import Bag, Item
from colorama import Fore, Style

from scriptum.screen import Screen

class Object(Item):
    def __init__(self, name, desc, aliases=[], isa=[], state=None, color=Fore.WHITE, undroppable=False, real_obj=None, action=None):
        super().__init__(name, *aliases)
        self.isa = isa
        self.desc = desc
        self.state = state
        self.color = color
        self.scene = None
        self.real_obj = real_obj
        self.__action = action
        self.undroppable = undroppable

        # Items on or in the Object that can be removed
        self.items = Bag()

        # Parts of the Object. They can be interacted with, but not removed.
        self.parts = Bag()

    def state_desc(self):
        desc = str(self)
        if self.state:
            desc += F" which is {self.state}"
        return desc

    # Example: object.is_a("door")
    def is_a(self, type_of_thing):
        found = False

        if type_of_thing in self.isa:
            found = True

        return found

    def activate(self):
        if self.__action:
            self.__action()

    def describe(self):
        if self.scene:
            self.scene.play()

        desc = ""
        if self.desc:
            desc += F"{self.desc}."

        if self.state:
            desc += F" It's {self.state}."

        for itm in self.items:
            desc += F" The {self} has a {itm} on it."

        for obj in self.parts:
            desc += F" The {self} has a {obj}."

        return desc

    def __str__(self):
        return Screen.colorize_text(self.name, fg=self.color)
