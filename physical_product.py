from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    """Class for Physical Product"""

    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def get_weight(self) -> float:
        """
        Function for returning the weight of the physical product
        """

        return self.__weight

    def display_product_info(self) -> None:
        """
        Function for printing physical product information
        """

        super().display_product_info()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        """
        Function for returning the physical product fulfilment information
        """

        return "Physical shipping is required."

    def calculate_shipping_cost(self) -> float:
        """
        Function for calculating and returning the shipping cost based on the product weight
        """

        shipping_cost_per_kg = 3.0
        return self.__weight * shipping_cost_per_kg