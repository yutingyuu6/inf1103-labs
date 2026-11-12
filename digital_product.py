from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    """Class for Digital Product"""

    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        """
        Function for returning the download size of the digital product
        """

        return self.__download_size

    def display_product_info(self) -> None:
        """
        Function for printing digital product information
        """

        super().display_product_info()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        """
        Function for returning the digital product fulfilment information
        """

        return "Digital download is available."