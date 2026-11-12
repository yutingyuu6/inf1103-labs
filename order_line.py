# Import Product class
from product import Product

class OrderLine:
    """Class for Order Line"""
    
    def __init__(self, product: Product, quantity: int):
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        """
        Function for calculating the subtotal of the order line.
        """

        return self.__product.get_price() * self.__quantity