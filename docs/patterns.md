# Design Patterns — CoffeeShopPro

CoffeeShopPro applies **three design patterns from two categories**:
- Structural: **Decorator**, **Facade**
- Behavioral: **Interpreter**

## Pattern 1 — Decorator (Structural)

**Module:** `decorator.py`

**Problem solved:** A customer must be able to add any combination of toppings 
(milk, sugar, whipped cream, caramel) to a beverage, and each topping adds cost. 
A naïve design would require a separate class for every possible combination.

**Alternative rejected:** *One subclass per combination* — e.g., `CoffeeWithMilk`, 
`CoffeeWithMilkAndSugar`, `CoffeeWithMilkAndSugarAndCream`, … With N toppings, this 
requires 2^N subclasses. For 4 toppings that's already 16 classes, and adding a 5th 
topping doubles it to 32.

**Why Decorator is better:** Each topping is a wrapper class. Four topping classes 
cover all combinations at runtime (Open/Closed Principle). Adding a new topping 
requires only one new class — no existing code changes.

## Pattern 2 — Facade (Structural)

**Module:** `facade.py`

**Problem solved:** The console UI needs to coordinate several subsystems: beverage 
construction, promo interpretation, and database persistence. If `main.py` called 
each subsystem directly, it would become tightly coupled and hard to change.

**Alternative rejected:** *Direct subsystem calls in `main.py`* — the UI module 
would need to know about `Coffee`, all four decorators, `PromoInterpreter`, and 
`Database`. Any change to a subsystem's API would ripple into the UI.

**Why Facade is better:** `CoffeeShopFacade` exposes simple methods 
(`order_coffee`, `add_topping`, `apply_promo`, `checkout`) that hide all subsystem 
details. If the database changes from SQLite to Postgres, only `facade.py` changes.

## Pattern 3 — Interpreter (Behavioral)

**Module:** `interpreter.py`

**Problem solved:** Promo codes are entered as strings ("HAPPYHOUR", "WEEKEND", …) 
and must be turned into numeric discount percentages. The mapping is data-driven and 
likely to grow.

**Alternative rejected:** *A long `if/elif` chain inside the Facade* — every new 
promo code edits the Facade, violating the Open/Closed Principle, and the discount 
logic becomes tangled with ordering logic.

**Why Interpreter is better:** Each promo code is a small expression object that 
"interprets" itself into a discount. Adding a new code means one line in the 
`PROMO_CODES` map — no logic changes.

## UML Class Diagram

(Insert the UML diagram image here — the one from Lab 2 updated to add 
`Database` and `Admin` classes. I will draw this in the next step.)