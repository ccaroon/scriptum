from adventurelib import set_context, get_context

class Context:
    ACTIVE = []

    def __init__(self, status, icon=''):
        self.__status = status
        self.__icon = icon

    @classmethod
    def clear(cls):
        cls.ACTIVE = []
        set_context(None)

    @classmethod
    def get(cls):
        stati = []
        for ctx in cls.ACTIVE:
            stati.append(str(ctx))

        return ' | '.join(stati)

    @classmethod
    def __set_raw_status(self):
        raw_stati = []
        for ctx in self.ACTIVE:
            raw_stati.append(ctx.status)        

        if raw_stati:
            set_context('.'.join(raw_stati))
        else:
            set_context(None)

    @classmethod
    def raw_status(self):
        return get_context()
    
    @classmethod
    def add(cls, ctx):
        cls.ACTIVE.append(ctx)
        cls.__set_raw_status()

    @classmethod
    def remove(cls, ctx):
        cls.ACTIVE.remove(ctx)
        cls.__set_raw_status()

    @property
    def status(self):
        return self.__status

    def activate(self):
        Context.add(self)

    def deactivate(self):
        Context.remove(self)

    def is_active(self):
        return self in Context.ACTIVE

    def __str__(self):
        s = self.status
        if self.__icon:
            s += F"({self.__icon})"

        return s
