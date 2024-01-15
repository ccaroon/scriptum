from adventurelib import set_context, get_context

from scriptum.context import Context

class ContextManager:
    __ACTIVE = []
    __CONTEXTS = {}

    @classmethod
    def create(cls, name, icon = ''):
        ctx = Context(name, icon)
        cls.__CONTEXTS[name] = ctx

        return ctx

    @classmethod
    def get(cls, name):
        return cls.__CONTEXTS.get(name)

    # @classmethod
    # def blah(cls):
    #     stati = []
    #     for ctx in cls.__ACTIVE:
    #         stati.append(str(ctx))

    #     return ' | '.join(stati)

    @classmethod
    def __set_raw_status(self):
        raw_stati = []
        for ctx in self.__ACTIVE:
            raw_stati.append(ctx.name)

        if raw_stati:
            set_context('.'.join(raw_stati))
        else:
            set_context(None)

    @classmethod
    def status(self):
        return get_context()

    @classmethod
    def activate(cls, ctx):
        cls.__ACTIVE.append(ctx)
        cls.__set_raw_status()

    @classmethod
    def deactivate(cls, ctx):
        cls.__ACTIVE.remove(ctx)
        cls.__set_raw_status()

    @classmethod
    def deactivate_all(cls):
        cls.__ACTIVE = []
        set_context(None)

    @classmethod
    def is_active(cls, ctx):
        return ctx in cls.__ACTIVE
