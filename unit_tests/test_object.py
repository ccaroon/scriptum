import colorama

import unittest
import os
import re

from scriptum.object import Object
from scriptum.screen import Screen
from scriptum.scene import Scene

class ObjectTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        self.scanner = Object(
            "Psi-Scan",
            "Psi-Scan - Model #345 | OS: v0.7.0",
            aliases=('scanner', 'psi-scan', 'psiscan'),
            isa=['gadget'],
            state="broken",
            color=colorama.Fore.RED,
            action=lambda: self.scanner.isa.append("chicken")
        )

        self.button = Object("button","A small, red button.")
        self.hair   = Object("hair", "A long, black hair.")
        self.dust   = Object("spec of dust", "A spec of dust.")

    def test_tostring(self):
        self.assertEqual(
            str(self.scanner),
            Screen.colorize_text("Psi-Scan", fg=colorama.Fore.RED)
        )

    def test_isa(self):
        self.assertFalse(self.scanner.is_a("potato"))

        self.assertTrue(self.scanner.is_a("gadget"))

    def test_activate(self):
        self.assertFalse(self.scanner.is_a("chicken"))

        self.scanner.activate()

        self.assertTrue(self.scanner.is_a("chicken"))

    def test_state_desc(self):
        self.assertEqual(
            self.scanner.state_desc(),
            F"{Screen.colorize_text('Psi-Scan', fg=colorama.Fore.RED)} which is broken"
        )

    def test_describe(self):
        # Basic
        expected_desc = F"{self.scanner.desc}. It's {self.scanner.state}."
        self.assertEqual(self.scanner.describe(), expected_desc)

        # With Items
        self.scanner.items.add(self.hair)
        self.scanner.items.add(self.dust)
        for itm in self.scanner.items:
            rx = re.compile(F"has a {re.escape(str(itm))} on it")
            self.assertRegex(self.scanner.describe(), rx)

        # With Parts
        self.scanner.parts.add(self.button)
        for itm in self.scanner.parts:
            rx = re.compile(F"has a {re.escape(str(itm))}")
            self.assertRegex(self.scanner.describe(), rx)

        # With a Scene
        self.scanner.items.clear()
        self.scanner.parts.clear()
        remove_hair = Scene("Remove the Hair")
        remove_hair.add_dialogue(
            F"You nimbly try to remove the {self.hair} from the {self.scanner}, but not matter how hard you try you just can seem to grasp it in your overly large fingers.",
            pause=False
        )
        self.scanner.scene = remove_hair
        self.assertEqual(self.scanner.describe(), expected_desc)











#
