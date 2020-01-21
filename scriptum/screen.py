import sys
from colorama import Back, Fore, Style

class Screen:

    @classmethod
    def colorize_text(cls, text, fg=Fore.LIGHTWHITE_EX, bg=Back.BLACK):
        return F"{bg}{fg}{text}{Style.RESET_ALL}"

    @classmethod
    def clear(cls, stream=sys.stdout):
        stream.write(F"{chr(27)}[2j\033c\x1bc")
