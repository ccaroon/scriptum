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
            isa=('gadget',),
            state="broken",
            color=colorama.Fore.RED
        )

        self.hair = Object("hair", "A long, black hair.")
        self.dust = Object("spec of dust", "A spec of dust.")

    def test_tostring(self):
        self.assertEqual(
            str(self.scanner), 
            Screen.colorize_text("Psi-Scan", fg=colorama.Fore.RED)
        )

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
        for itm in [self.dust, self.hair]:
            rx = re.compile(F"has a {re.escape(str(itm))} on it")
            self.assertRegex(self.scanner.describe(), rx)

        # With a Scene
        self.scanner.items.clear()
        remove_hair = Scene("Remove the Hair")
        remove_hair.add_dialogue(
            F"You nimbly try to remove the {self.hair} from the {self.scanner}, but not matter how hard you try you just can seem to grasp it in your overly large fingers.", 
            pause=False
        )
        self.scanner.scene = remove_hair
        self.assertEqual(self.scanner.describe(), expected_desc)











# 
