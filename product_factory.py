# Import Product, PhysicalProduct, DigitalProduct and Supplier classes
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class ProductFactory:
    """Class for Product Factory"""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, extra: float, supplier: Supplier) -> Product:
        """Function for creating the products."""

        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra, supplier)

        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra, supplier)

        else:
            raise ValueError(f"Unknown product type: {product_type}")