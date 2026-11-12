from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

def show_product_details(product: Product) -> None:
    """
    Function for displaying product details
    """

    product.display_product_info()
    print(product.get_fulfilment_info())

supplier = Supplier("S001", "Tech Supplies Inc.", "tech_supplies@email.com")

physical_product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5, supplier)

digital_product = DigitalProduct("P002", "E-book", 19.9, 30, 30.0, supplier)

show_product_details(physical_product)
show_product_details(digital_product)