import unittest
import os
from scriptum.object import Object
from scriptum.inventory import Inventory

class InventoryTest(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        car = Object(
            "Toy Car",
            "An old Lotus Elise sports car from 2042. This one's got a sunroof.",
            isa=("toy")
        )

        self.inventory.add(car)

    def test_contains_some_sort_of(self):
        self.assertTrue(self.inventory.contains_some_sort_of("toy"))
