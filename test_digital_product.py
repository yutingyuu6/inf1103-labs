from digital_product import DigitalProduct

product = DigitalProduct("D001", "E-book", 19.99, 100, 15.0)

product.display_product_info()

print(product.get_fulfilment_info())
print(f"Download Size: {product.get_download_size():.2f} MB")