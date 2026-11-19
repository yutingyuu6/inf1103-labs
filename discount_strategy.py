from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """Abstract class for discount strategies"""

    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    """
    Class for NoDiscount, 
    inherited from base class DiscountStrategy
    """

    def apply(self, total: float) -> float:
        """Function for returning the total unchanged."""
        return total

class PercentageDiscount(DiscountStrategy):
    """
    Class for PercentageDiscount,
    inherited from base class DiscountStrategy
    """

    def __init__(self, percentage: float):
        self.__percentage = percentage

    def get_percentage(self) -> float:
        return self.__percentage

    def apply(self, total: float) -> float:
        """
        Function for taking a percentage when created.
        e.g. PercentageDiscount(10) takes 10% off.
        """
        return total * (1 - self.__percentage / 100)

class BulkDiscount(DiscountStrategy):
    """
    Class for BulkDiscount,
    inherited from base class DiscountStrategy
    """

    def __init__(self, threshold: float, amount: float):
        self.__threshold = threshold
        self.__amount = amount

    def get_threshold(self) -> float:
        return self.__threshold

    def get_amount(self) -> float:
        return self.__amount

    def apply(self, total: float) -> float:
        """
        Function for taking a threshold and an amount.
        e.g. BulkDiscount(200, 20) takes 20 off any total of 200 or more.
        """
        return total - self.__amount if total >= self.__threshold else total

class StudentDiscount(DiscountStrategy):
    """
    Class for StudentDiscount,
    inherited from base class DiscountStrategy
    """

    def apply(self, total: float) -> float:
        """
        Function for calculating after 5% student discount.
        """
        
        return total * 0.95