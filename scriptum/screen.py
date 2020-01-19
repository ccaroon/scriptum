from colorama import Back, Fore, Style

class Screen:

    @classmethod
    def colorize(text, fg=Fore.LIGHTWHITE_EX, bg=Back.BLACK):
        return F"{bg}{fg}{text}{Style.RESET_ALL}"

    @classmethod
    def clear_screen():
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
