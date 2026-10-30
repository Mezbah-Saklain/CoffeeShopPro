import unittest
from admin import Admin
from database import Database

class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.admin = Admin(Database(":memory:"))  # isolated DB per test

    def test_add_valid_item(self):
        self.assertTrue(self.admin.add_item("Latte", 3.50, "Drink"))
        self.assertEqual(len(self.admin.list_items()), 1)

    def test_reject_negative_price(self):
        self.assertFalse(self.admin.add_item("Bad", -1.0, "Drink"))

    def test_reject_empty_name(self):
        self.assertFalse(self.admin.add_item("", 3.0, "Drink"))