import unittest
from scriptum.context_manager import ContextManager

class ContextManagerTest(unittest.TestCase):

    def setUp(self):
        ContextManager.deactivate_all()

    def test_basic(self):
        ctx = ContextManager.create("Locked In", '🔒')

        locked = ContextManager.get("Locked In")
        self.assertEqual(locked, ctx)

        self.assertFalse(ContextManager.is_active(ctx))
        self.assertIsNone(ContextManager.status())

        ContextManager.activate(ctx)
        self.assertTrue(ContextManager.is_active(ctx))
        self.assertEqual(ContextManager.status(), "Locked In")

        ContextManager.deactivate(ctx)
        self.assertFalse(ContextManager.is_active(ctx))
        self.assertIsNone(ContextManager.status())

    def test_multiple(self):
        dark = ContextManager.create("In The Dark", '🌑')
        snow = ContextManager.create("Snowing", '❄️')

        ContextManager.activate(snow)
        self.assertEqual(ContextManager.status(), "Snowing")

        ContextManager.activate(dark)
        self.assertEqual(ContextManager.status(), "Snowing.In The Dark")

        ContextManager.deactivate(snow)
        self.assertEqual(ContextManager.status(), "In The Dark")
