from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str: ...
    @abstractmethod
    def get_cost(self) -> float: ...

class Coffee(Beverage):
    def __init__(self, base_cost: float = 2.00):
        self._base_cost = base_cost
    def get_description(self) -> str:
        return "Coffee"
    def get_cost(self) -> float:
        return self._base_cost

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    def get_description(self) -> str:
        return self._beverage.get_description()
    def get_cost(self) -> float:
        return self._beverage.get_cost()

class MilkDecorator(BeverageDecorator):
    COST = 0.50
    def get_description(self): return self._beverage.get_description() + " + Milk"
    def get_cost(self): return self._beverage.get_cost() + self.COST

class SugarDecorator(BeverageDecorator):
    COST = 0.20
    def get_description(self): return self._beverage.get_description() + " + Sugar"
    def get_cost(self): return self._beverage.get_cost() + self.COST

class WhippedCreamDecorator(BeverageDecorator):
    COST = 0.70
    def get_description(self): return self._beverage.get_description() + " + Whipped Cream"
    def get_cost(self): return self._beverage.get_cost() + self.COST

class CaramelDecorator(BeverageDecorator):
    COST = 0.60
    def get_description(self): return self._beverage.get_description() + " + Caramel"
    def get_cost(self): return self._beverage.get_cost() + self.COST