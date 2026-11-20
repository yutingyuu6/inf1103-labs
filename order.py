# Import Product, OrderLine, DiscountStrategy and NoDiscount classes
from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount


class Order:
    """Class for Order"""

    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        """
        Function for adding an order line.
        """

        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        """
        Function for removing an order line.
        """

        for order_line in self.order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.order_lines.remove(order_line)
                return

        print(f"Product {product_id} not found in order.")
    
    def calculate_total(self) -> float:
        """
        Function for adding up the order line subtotals and passes the result to the discount strategy’s apply() method.
        """

        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)