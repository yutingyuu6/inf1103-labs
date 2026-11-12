# Import Product and OrderLine classes
from product import Product
from order_line import OrderLine


class Order:
    """Class for Order"""

    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        """
        Function for adding an order line.
        """

        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        """
        Function for calculating the total of the order.
        """

        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
            
        return total