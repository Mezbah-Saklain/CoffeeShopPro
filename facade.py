from decorator import Coffee, MilkDecorator, SugarDecorator, WhippedCreamDecorator, CaramelDecorator
from interpreter import PromoInterpreter
from database import Database

class CoffeeShopFacade:
    def __init__(self, db: Database = None):
        self._db = db or Database()
        self._order = None
        self._interpreter = PromoInterpreter()

    def order_coffee(self):
        if self._order:
            return "You already have an order."
        self._order = Coffee()
        return f"Coffee ordered: ${self._order.get_cost():.2f}"

    def add_topping(self, name: str) -> str:
        if not self._order:
            return "Order a coffee first."
        mapping = {
            "milk": MilkDecorator, "sugar": SugarDecorator,
            "cream": WhippedCreamDecorator, "caramel": CaramelDecorator,
        }
        dec = mapping.get(name.lower())
        if not dec:
            return f"Unknown topping: {name}"
        self._order = dec(self._order)
        return f"Added {name}: +${dec.COST:.2f}"

    def apply_promo(self, code: str) -> str:
        if not self._order:
            return "Order a coffee first."
        before = self._order.get_cost()
        pct = self._interpreter.discount_percent(code)
        after = self._interpreter.apply(code, before)
        if pct == 0:
            return f"Invalid promo: {code}"
        self._order = Coffee(base_cost=after)
        return f"Applied {pct:.0f}% off. New total: ${after:.2f}"

    def checkout(self) -> str:
        if not self._order:
            return "No order to checkout."
        desc = self._order.get_description()
        total = self._order.get_cost()
        self._db.save_order(desc, total)
        self._order = None
        return f"Receipt: {desc} | Total: ${total:.2f}"