import unittest
from scriptum.context import Context

class ContextTest(unittest.TestCase):
    def test_tostring(self):
        ctx = Context("Zero'd Out", '0')
        self.assertEqual(str(ctx), "Zero'd Out(0)")

    def test_properties(self):
        name = "Locked In"
        icon = '🔒'
        ctx = Context(name, icon)

        self.assertEqual(ctx.name, name)
        self.assertEqual(ctx.icon, icon)
