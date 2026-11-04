from physical_product import PhysicalProduct

product = PhysicalProduct("P001", "Laptop", 1200.0, 15)

product.display_product_info()

print(product.get_fulfilment_info())
print(f"Weight: {product.get_weight():.2f} kg")