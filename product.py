class Product:
    """Class for Product"""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity: int):
        """
        Function for updating stock quantity
        If quantity is lower than zero, ValueError is raised and error message is printed.
        If quantity is non-negative, product stock is updated.
        """

        if quantity < 0:
            raise ValueError("Error: Stock Quantity cannot be negative.")

        self.__stock = quantity

    def display_product_info(self):
        """Function for printing product information"""
        
        print(
            f"ID: {self.__product_id} | ",
            f"Name: {self.__name} | ",
            f"Price: ${self.__price:.2f} | ",
            f"Stock: {self.__stock}"
        )