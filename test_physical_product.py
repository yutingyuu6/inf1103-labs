from physical_product import PhysicalProduct

product1 = PhysicalProduct("P001", "Laptop", 1200.0, 15, 4.5)
product2 = PhysicalProduct("P002", "Mouse", 25.0, 50, 0.5)

product1.display_product_info()
print("Shipping Cost: $", product1.calculate_shipping_cost())
print()

product2.display_product_info()
print("Shipping Cost: $", product2.calculate_shipping_cost())
print()
