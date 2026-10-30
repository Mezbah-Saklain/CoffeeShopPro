from facade import CoffeeShopFacade
from admin import Admin


def print_menu():
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║         ☕  WELCOME TO THE COFFEE SHOP  ☕       ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  1. Order Coffee      2. Add Milk                ║")
    print("║  3. Add Sugar         4. Add Whipped Cream       ║")
    print("║  5. Add Caramel       6. Apply Promo Code        ║")
    print("║  7. Checkout          8. Admin: Add Menu         ║")
    print("║  9. View Past Orders  0. Exit                    ║")
    print("╚══════════════════════════════════════════════════╝")


def main():
    shop = CoffeeShopFacade()
    admin = Admin(shop._db)

    while True:
        print_menu()
        ch = input("  ➤ Your choice: ").strip()
        print()

        if ch == "1":
            print("  ✔ " + shop.order_coffee())
        elif ch == "2":
            print("  ✔ " + shop.add_topping("milk"))
        elif ch == "3":
            print("  ✔ " + shop.add_topping("sugar"))
        elif ch == "4":
            print("  ✔ " + shop.add_topping("cream"))
        elif ch == "5":
            print("  ✔ " + shop.add_topping("caramel"))
        elif ch == "6":
            code = input("  Promo code (HAPPYHOUR/WELCOME/STUDENT/WEEKEND/FIRSTORDER): ").strip()
            print("  ✔ " + shop.apply_promo(code))
        elif ch == "7":
            print("  ✔ " + shop.checkout())
        elif ch == "8":
            n = input("  Name: ").strip()
            p = float(input("  Price: ").strip())
            c = input("  Category (Drink/Topping/Other): ").strip()
            print("  ✔ Added!" if admin.add_item(n, p, c) else "  ✘ Invalid input")
        elif ch == "9":
            orders = shop._db.get_orders()
            if not orders:
                print("  (no orders yet)")
            else:
                print("  ── ORDER HISTORY ──")
                for i, (d, t) in enumerate(orders, 1):
                    print(f"  {i}. {d:<30} ${t:.2f}")
        elif ch == "0":
            print("  👋 Bye! Thanks for visiting.")
            break
        else:
            print("  ✘ Invalid choice. Try again.")


if __name__ == "__main__":
    main()