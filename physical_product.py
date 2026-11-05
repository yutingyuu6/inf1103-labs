from product import Product

class PhysicalProduct(Product):
    """Class for Physical Product"""

    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        """
        Function for returning the weight of the physical product
        """

        return self.__weight

    def display_product_info(self):
        """
        Function for printing physical product information
        """

        super().display_product_info()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        """
        Function for returning the physical product fulfilment information
        """

        return "Physical shipping is required."