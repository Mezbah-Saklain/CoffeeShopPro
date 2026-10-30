from abc import ABC, abstractmethod

PROMO_CODES = {
    "HAPPYHOUR": 20,
    "WELCOME": 10,
    "STUDENT": 15,
    "WEEKEND": 25,
    "FIRSTORDER": 30,
}

class Expression(ABC):
    @abstractmethod
    def interpret(self) -> float: ...

class PromoExpression(Expression):
    def __init__(self, code: str):
        self._code = code.strip().upper()
    def interpret(self) -> float:
        return PROMO_CODES.get(self._code, 0.0)

class PromoInterpreter:
    def discount_percent(self, code: str) -> float:
        return PromoExpression(code).interpret()
    def apply(self, code: str, cost: float) -> float:
        pct = self.discount_percent(code)
        return round(cost * (1 - pct / 100), 2)