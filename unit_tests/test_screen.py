import colorama
from io import StringIO
import unittest
import os
from scriptum.screen import Screen

class ScreenTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_colorize(self):
        msg = Screen.colorize_text("Hello, World!", fg=colorama.Fore.GREEN, bg=colorama.Back.BLUE)
        self.assertEqual(msg, F"{colorama.Back.BLUE}{colorama.Fore.GREEN}Hello, World!{colorama.Style.RESET_ALL}")

    def test_bold(self):
        msg = Screen.bold("Hello, World!")
        self.assertEqual(msg, F"{colorama.Style.BRIGHT}Hello, World!{colorama.Style.RESET_ALL}")

    def test_clear(self):
        output = StringIO()
        Screen.clear(stream=output)

        self.assertEqual(output.getvalue(), F"{chr(27)}[2j\033c\x1bc")

        output.close()
