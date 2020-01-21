import unittest
import os
from scriptum.object import Object
from scriptum.room import Room

class RoomTest(unittest.TestCase):

    def setUp(self):
        north = Room("North of the Void", "-")
        east  = Room("East of the Void",  "-")
        south = Room("South of the Void", "-")
        west  = Room("West of the Void",  "-")

        no_tea = Object("No Tea", "-")
        no_window = Object("UnWindow", "-")

        self.the_void = Room(
            "The Void",
            "No light. No dark. No air. No thing. Nothing.",
            items=[no_tea],
            objects=[no_window],
            north=north, east=east, south=south, west=west,
        )

    def test_tostring(self):
        exp_string = F"""--- {self.the_void.name} ---
{self.the_void.description}"""

        self.assertEqual(str(self.the_void), exp_string)

    def test_items(self):
        self.assertTrue(self.the_void.items.find("No Tea"))

    def test_objects(self):
        self.assertTrue(self.the_void.objects.find("UnWindow"))
