from product import Product

class Inventory:
    """Class for Inventory"""

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """
        Function for adding product
        If duplicate product_id exists, False is returned.
        If product_id is unique, the product is added to list and True is returned.
        """

        if self.search_product(product.get_product_id()) is not None:
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        """
        Function for searching product
        If the product_id exists, the product is returned.
        If the product_id does not exists, None value is returned.
        """

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self) -> None:
        """
        Function for displaying information of all products
        If no product exists, inventory is empty message is printed.
        Else, if the product exists, for every existing product, the display_product_info() function is called to print the information of each product.
        """

        print("\nCurrent Inventory")
        print("-" * 48)

        if not self.__products:
            print("Inventory is empty.")

        else:
            for product in self.__products:
                product.display_product_info()

        print("-" * 48)

    def get_products(self):
        """
        Function for returning a copy of the list of products
        """

        return self.__products.copy()

    def remove_product(self, product_id: str) -> None:
        """
        Function for removing product
        For every product in the inventory, if the product_id exists, the product is removed from the inventory.
        If the product_id does not exist, product_id not found message is printed.
        """

        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                print(f"Product {product_id} has been removed from the inventory.")
                return

        print(f"Product {product_id} not found in the inventory.")