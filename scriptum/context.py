class Context:
    def __init__(self, name, icon=''):
        self.__name = name
        self.__icon = icon

    @property
    def name(self):
        return self.__name

    @property
    def icon(self):
        return self.__icon

    def __str__(self):
        output = self.name
        if self.icon:
            output += F"({self.icon})"

        return output
