import unittest
from decorator import Coffee, MilkDecorator, SugarDecorator, WhippedCreamDecorator

class TestDecorator(unittest.TestCase):
    def test_base_coffee_cost(self):
        self.assertEqual(Coffee().get_cost(), 2.00)

    def test_milk_adds_half_dollar(self):
        self.assertAlmostEqual(MilkDecorator(Coffee()).get_cost(), 2.50)

    def test_sugar_stacks_with_milk(self):
        b = SugarDecorator(MilkDecorator(Coffee()))
        self.assertAlmostEqual(b.get_cost(), 2.70)

    def test_description_reflects_toppings(self):
        b = WhippedCreamDecorator(MilkDecorator(Coffee()))
        self.assertIn("Milk", b.get_description())
        self.assertIn("Whipped Cream", b.get_description())