import unittest
from unittest.mock import MagicMock
from facade import CoffeeShopFacade

class TestFacadeWithMock(unittest.TestCase):
    def test_checkout_saves_to_db(self):
        mock_db = MagicMock()
        shop = CoffeeShopFacade(db=mock_db)
        shop.order_coffee()
        shop.add_topping("milk")
        shop.checkout()
        # Verify DB was asked to save — without touching a real database
        mock_db.save_order.assert_called_once()
        args, _ = mock_db.save_order.call_args
        self.assertAlmostEqual(args[1], 2.50)

    def test_cannot_add_topping_without_order(self):
        shop = CoffeeShopFacade(db=MagicMock())
        self.assertIn("first", shop.add_topping("milk").lower())

    def test_invalid_promo_leaves_cost_unchanged(self):
        shop = CoffeeShopFacade(db=MagicMock())
        shop.order_coffee()
        shop.apply_promo("NOTREAL")
        self.assertAlmostEqual(shop._order.get_cost(), 2.00)