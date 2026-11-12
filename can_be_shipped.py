from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    """Abstract class interface for products that can be shipped"""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Function for calculating and returning the shipping cost"""
        pass