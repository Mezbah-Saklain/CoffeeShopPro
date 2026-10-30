from database import Database

class Admin:
    def __init__(self, db: Database):
        self._db = db
    def add_item(self, name: str, price: float, category: str) -> bool:
        if price <= 0 or not name.strip():
            return False
        self._db.add_menu_item(name, price, category)
        return True
    def list_items(self):
        return self._db.get_menu()