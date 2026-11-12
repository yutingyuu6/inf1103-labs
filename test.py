from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier
from order import Order
from order_line import OrderLine

def test_product_supplier_association():

    supplier = Supplier("S001", "Tech Supplies Inc.", "tech_supplies@email.com")

    assert supplier is not None

    product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5, supplier)

    assert product.get_supplier() is supplier

    print("Test 1 passed")

test_product_supplier_association()

def test_inventory_aggregation():

    inventory1 = Inventory()
    inventory2 = Inventory()

    supplier = Supplier("S001", "Tech Supplies Inc.", "tech_supplies@email.com")

    product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5, supplier)

    assert inventory1.add_product(product) is True
    assert inventory1.find_product("P001") is product
    inventory1.remove_product("P001")
    assert inventory1.find_product("P001") is None
    assert product.get_name() == "Laptop"
    assert inventory2.add_product(product) is True
    assert inventory2.find_product("P001") is product

    print("Test 2 passed")

test_inventory_aggregation()

def test_order():

    supplier = Supplier("S001", "Tech Supplies Inc.", "tech_supplies@email.com")

    product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5, supplier)

    order = Order("O001")
    order.add_order_line(product, 2)
    assert len(order.order_lines) == 1
    order_line = order.order_lines[0]
    assert order_line.get_product() is product
    assert order_line.get_quantity() == 2
    assert order_line.calculate_subtotal() == 2400.0
    assert order.calculate_total() == 2400.0
    order.remove_order_line("P001")
    assert len(order.order_lines) == 0
    assert product.get_name() == "Laptop"

    print("Test 3 passed")

test_order()

def show_product_details(product: Product) -> None:
    """
    Function for displaying product details
    """

    product.display_product_info()
    print(product.get_fulfilment_info())
    print("Test 4 passed")

def test_polymorphism():
    """
    Function for testing polymorphism.
    """

    supplier = Supplier("S001", "Tech Supplies Inc.", "tech_supplies@email.com")

    physical_product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5, supplier)
    digital_product = DigitalProduct("P002", "E-book", 19.9, 30, 30.0, supplier)

    inventory = Inventory()

    inventory.add_product(physical_product)
    inventory.add_product(digital_product)

    inventory.display_all()

    print("Test 5 passed")

test_polymorphism()


if __name__ == "__main__":
    test_product_supplier_association()
    test_inventory_aggregation()
    test_order()

    supplier = Supplier("S001", "Tech Supplies Inc.", "tech_supplies@email.com")

    physical_product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5, supplier)

    digital_product = DigitalProduct("P002", "E-book", 19.9, 30, 30.0, supplier)

    show_product_details(physical_product)
    show_product_details(digital_product)

    test_polymorphism()