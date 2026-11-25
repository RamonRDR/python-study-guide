"""Protect a stock invariant and depend on a small abstraction."""
from abc import ABC, abstractmethod


class Stock:
    def __init__(self, quantity: int) -> None:
        if type(quantity) is not int:
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = quantity

    @property
    def quantity(self) -> int:
        return self._quantity

    def remove(self, amount: int) -> None:
        if type(amount) is not int:
            raise TypeError("amount must be an integer")
        if not 0 <= amount <= self._quantity:
            raise ValueError("invalid amount")
        self._quantity -= amount


class StockReader(ABC):
    @abstractmethod
    def available(self) -> int:
        """Return available quantity."""


class InMemoryStockReader(StockReader):
    def __init__(self, stock: Stock) -> None:
        self.stock = stock

    def available(self) -> int:
        return self.stock.quantity


def remaining(reader: StockReader) -> int:
    return reader.available()


if __name__ == "__main__":
    stock = Stock(3)
    stock.remove(2)
    print(remaining(InMemoryStockReader(stock)))
