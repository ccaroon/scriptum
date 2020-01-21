import unittest
import os
from scriptum.context import Context

class ContextTest(unittest.TestCase):

    def setUp(self):
        Context.clear()

    def test_tostring(self):
        ctx = Context("Zero'd Out", '0')
        self.assertEqual(str(ctx), "Zero'd Out(0)")

    def test_instance(self):
        ctx = Context("Locked In", '🔒')
        self.assertFalse(ctx.is_active())
        self.assertEqual(ctx.status, "Locked In")
        self.assertEqual(Context.get(), "")

        ctx.activate()
        self.assertTrue(ctx.is_active())
        self.assertEqual(Context.get(), "Locked In(🔒)")

        ctx.deactivate()
        self.assertFalse(ctx.is_active())
        self.assertEqual(Context.get(), "")
    
    def test_multiple(self):
        dark = Context("In The Dark", '🌑')
        snow = Context("Snowing", '❄️')

        Context.add(snow)
        self.assertEqual(Context.get(), "Snowing(❄️)")
        self.assertEqual(Context.raw_status(), "Snowing")

        Context.add(dark)
        self.assertEqual(Context.get(), "Snowing(❄️) | In The Dark(🌑)")
        self.assertEqual(Context.raw_status(), "Snowing.In The Dark")

        Context.remove(snow)
        self.assertEqual(Context.get(), "In The Dark(🌑)")
        self.assertEqual(Context.raw_status(), "In The Dark")
