import sys
import pyfiglet
from abc import ABC, abstractmethod

from scriptum.screen import Screen

class Scene:

    def __init__(self, name, on_going=False):
        self.__name = name
        self.__events = []

        # Number of times allowed to run
        self.__run_count = 1
        if on_going:
            self.__run_count = 9999999

    def add_action(self, action, pause=True):
        self.__events.append(Scene.Action(action, pause))

    def add_dialogue(self, statement, enlarge=False, color=None, pause=True, stream=sys.stdout):
        text = statement
        if enlarge:
            text = pyfiglet.figlet_format(statement)

        if color:
            text = Screen.colorize_text(text, fg=color)

        self.__events.append(Scene.Dialogue(text, pause, stream=stream))

    def play(self, **kwargs):
        if self.__run_count > 0:
            self.__run_count -= 1

            if kwargs.get("clear_screen", False):
                Screen.clear()

            for i, event in enumerate(self.__events):
                event.run()
                # prompt = F"{i+1}/{count}".center(80, "-")
                # input(prompt)
                if event.pause:
                    input()

    # Sub Classes
    class Event(ABC):
        def __init__(self, pause):
            self.pause = pause

        @abstractmethod
        def run(self):
            pass

    class Action(Event):
        def __init__(self, action, pause=True):
            self.__action = action
            super().__init__(pause)

        def run(self):
            self.__action()

    class Dialogue(Event):
        def __init__(self, statement, pause=True, stream=sys.stdout):
            self.__stmt = statement
            self.__stream = stream
            super().__init__(pause)

        def run(self):
            print(self.__stmt, file=self.__stream)
