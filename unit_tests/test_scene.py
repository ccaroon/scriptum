import colorama
import unittest
import os
import pyfiglet

from io import StringIO
from scriptum.screen import Screen
from scriptum.scene import Scene

class SceneTest(unittest.TestCase):

    def setUp(self):
        self.scene = Scene("Test Scene")
        self.og_scene = Scene("Test Scene", on_going=True)

    def test_dialog(self):
        output = StringIO()

        self.scene.add_dialogue("Hello, World!", pause=False, stream=output)
        self.scene.play()
        
        self.assertEqual(output.getvalue(), "Hello, World!\n")
        output.close()

    def test_dialog_color(self):
        # In ColorVision
        output = StringIO()
        self.scene.add_dialogue("Bring The Noise", color=colorama.Fore.GREEN, pause=False, stream=output)

        self.scene.play()
        exp_dialog = Screen.colorize_text("Bring The Noise", fg=colorama.Fore.GREEN)
        self.assertEqual(output.getvalue(), F"{exp_dialog}\n")

        output.close()

    def test_dialog_enlarge(self):
        # Large Print
        output = StringIO()
        self.scene.add_dialogue("Frog Blast the Vent Core!", enlarge=True, pause=False, stream=output)

        self.scene.play()
        exp_output = pyfiglet.figlet_format("Frog Blast the Vent Core!")
        self.assertEqual(output.getvalue(), F"{exp_output}\n")

        output.close()


    def test_action(self):
        self.the_answer = 0
        def solve_it():
            self.the_answer += 42

        self.assertEqual(self.the_answer, 0)
        self.scene.add_action(solve_it, pause=False)

        self.scene.play()
        self.assertEqual(self.the_answer, 42)

        # Should NOT run again
        self.scene.play()
        self.assertEqual(self.the_answer, 42)

    def test_action_on_going(self):
        self.counter = 0
        def call_me():
            self.counter += 1

        self.og_scene.add_action(call_me, pause=False)

        self.assertEqual(self.counter, 0)
        
        self.og_scene.play()
        self.assertEqual(self.counter, 1)

        # Play it again, Sam!
        self.og_scene.play()
        self.assertEqual(self.counter, 2)







# 
