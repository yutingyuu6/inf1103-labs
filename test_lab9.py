# Test code for Lab 9

# Import inspect and pytest modules
import inspect
import pytest

# Import the classes
from product import Product
from inventory import Inventory
from order import Order
from order_line import OrderLine
from supplier import Supplier
from discount_strategy import (DiscountStrategy, NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount)
from product_factory import ProductFactory
from main import get_positive_float, load_products

@pytest.fixture
def supplier():
    return Supplier("S1", "Supplier A", "suppliera@email.com")

@pytest.fixture
def order_250(supplier):
    product = ProductFactory.create("physical", "P1", "Item", 125.0, 10, 1.0, supplier)
    order = Order("01")
    order.add_order_line(product, 2)
    return order

# ---------- Test Discount Strategies ----------
def test_default_is_no_discount(order_250):
    assert order_250.calculate_total() == 250

def test_bulk_discount(order_250):
    order_250.set_discount(BulkDiscount(200, 20))
    assert order_250.calculate_total() == 230

def test_bulk_below_threshold(order_250):
    order_250.set_discount(BulkDiscount(300, 20))
    assert order_250.calculate_total() == 250

def test_set_discount_changes_strategy(order_250):
    order_250.set_discount(BulkDiscount(200, 20))
    order_250.set_discount(PercentageDiscount(10))
    assert order_250.calculate_total() == 225

def test_new_strategy_needs_no_order_change(order_250):
    order_250.set_discount(StudentDiscount())
    assert order_250.calculate_total() == pytest.approx(237.5)

def test_order_has_no_discount_branching():
    assert "elif" not in inspect.getsource(Order.calculate_total)

def test_strategies_inherit_base():
    for cls in (NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount):
        assert issubclass(cls, DiscountStrategy)

# ---------- Test Product Factory ----------
def test_factory_returns_product(supplier):
    assert isinstance(ProductFactory.create("digital", "D1", "Application", 10.0, 1, 5.0, supplier), Product)

def test_factory_unknown_type(supplier):
    with pytest.raises(ValueError, match = "Unknown product type: service"):
        ProductFactory.create("service", "S1", "Install", 30.0, 5, 0.0, supplier)

# ---------- Test Validations ----------
@pytest.mark.parametrize("price, stock", [(0, 5), (-1, 5), (10, -1)])
def test_invalid_product_rejected(supplier, price, stock):
    with pytest.raises(ValueError):
        ProductFactory.create("physical", "P1", "X", price, stock, 1.0, supplier)

def test_update_stock_negative_rejected(supplier):
    p = ProductFactory.create("physical", "P1", "X", 10.0, 5, 1.0, supplier)
    with pytest.raises(ValueError):
        p.update_stock(-1)

@pytest.mark.parametrize("qty", [0, -3])
def test_invalid_order_line_quantity(supplier, qty):
    p = ProductFactory.create("physical", "P1", "X", 10.0, 5, 1.0, supplier)
    with pytest.raises(ValueError):
        OrderLine(p, qty)

# ---------- Test Exception Handling ----------
def test_get_positive_float_asks_again(monkeypatch, capsys):
    inputs = iter(["abc", "-5", "12.50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_positive_float("Price: ") == 12.5
    out = capsys.readouterr().out
    assert "valid number" in out
    assert "greater than zero" in out

PRODUCTS_CSV = (
    "product_type,product_id,name,price,stock_quantity\n"
    "physical,P001,Desk Lamp,25.00,10\n"
    "digital,D001,Photo Editor,49.90,100\n"
    "service,S001,Installation,30.00,5\n"
    "physical,P002,Office Chair,abc,3\n"
    "physical,P003,Monitor Stand,39.50,7\n"
)

def test_load_products_skips_bad_rows(tmp_path, supplier, capsys):
    f = tmp_path / "products.csv"
    f.write_text(PRODUCTS_CSV)
    inv = Inventory()
    load_products(str(f), inv, supplier)
    out = capsys.readouterr().out

    assert len(inv.get_products()) == 3
    assert "3 products loaded." in out
    assert "Unknown product type: service" in out
    assert "Load attempt finished." in out

def test_load_products_missing_file(tmp_path, supplier, capsys):
    inv = Inventory()
    load_products(str(tmp_path / "nope.csv"), inv, supplier)
    out = capsys.readouterr().out

    assert "not found" in out
    assert "Load attempt finished." in out
    assert len(inv.get_products()) == 0