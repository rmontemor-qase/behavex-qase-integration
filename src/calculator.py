"""Tiny calculator used as a system-under-test for the sample BDD suite."""


class Calculator:
    def __init__(self) -> None:
        self._value: float = 0.0

    @property
    def value(self) -> float:
        return self._value

    def reset(self) -> None:
        self._value = 0.0

    def add(self, x: float) -> float:
        self._value += x
        return self._value

    def subtract(self, x: float) -> float:
        self._value -= x
        return self._value

    def multiply(self, x: float) -> float:
        self._value *= x
        return self._value

    def divide(self, x: float) -> float:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self._value /= x
        return self._value
