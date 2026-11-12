# MIT License
#
# Copyright (c) 2026 <Team name / member names>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Store Inventory: a small inventory manager for a shop.

The inventory maps a product code to its data:
    {"A1": {"name": "Notebook", "price": 2.5, "stock": 40}, ...}
"""

Inventory = dict[str, dict]


# --- Member 1 ---------------------------------------------------------------
def add_product(
    inventory: Inventory, code: str, name: str, price: float, stock: int
) -> dict:
    """Add a new product to the inventory (modified in place).
    Args:
        inventory: Inventory to modify.
        code: Unique, non-empty product code (e.g. "A1").
        name: Product name.
        price: Unit price, 0 or more.
        stock: Initial units, 0 or more.
    Returns:
        The stored product as a dict.
    Raises:
        ValueError: Empty or repeated code, or negative price or stock.
    Example:
        >>> inv = {}
        >>> add_product(inv, "A1", "Notebook", 2.5, 40)
        {'name': 'Notebook', 'price': 2.5, 'stock': 40}
    """
    code = code.strip()
    if not code:
        raise ValueError("Product code cannot be empty")
    if code in inventory:
        raise ValueError(f"Product already exists: {code}")
    if price < 0 or stock < 0:
        raise ValueError("Price and stock must be >= 0")
    inventory[code] = {
        "name": name.strip(),
        "price": round(float(price), 2),
        "stock": int(stock),
    }
    return inventory[code]


# --- Member 2 ---------------------------------------------------------------
def search_products(inventory: Inventory, query: str) -> list[tuple[str, dict]]:
    """Find products whose code or name contains the query (ignores case).
    Args:
        inventory: Inventory to search.
        query: Text to look for, e.g. "pen".
    Returns:
        (code, product) pairs sorted by code; empty list if no match.
    Example:
        >>> inv = {"B2": {"name": "Pen", "price": 0.8, "stock": 3}}
        >>> search_products(inv, "PEN")
        [('B2', {'name': 'Pen', 'price': 0.8, 'stock': 3})]
    """
    text = query.strip().lower()
    matches = [
        (code, product)
        for code, product in inventory.items()
        if text in code.lower() or text in product["name"].lower()
    ]
    return sorted(matches, key=lambda item: item[0])


# --- Member 3 ---------------------------------------------------------------
def update_stock(inventory: Inventory, code: str, change: int) -> int:
    """Add (delivery) or remove (sale) units of a product (modified in place).
    Args:
        inventory: Inventory to modify.
        code: Code of an existing product.
        change: Units to add (positive) or remove (negative).
    Returns:
        The new stock level.
    Raises:
        KeyError: Unknown product.
        ValueError: The new stock would be negative.
    Example:
        >>> inv = {"B2": {"name": "Pen", "price": 0.8, "stock": 3}}
        >>> update_stock(inv, "B2", 20)
        23
    """
    if code not in inventory:
        raise KeyError(f"Unknown product: {code}")
    new_stock = inventory[code]["stock"] + change
    if new_stock < 0:
        raise ValueError(f"Not enough stock for {code}")
    inventory[code]["stock"] = new_stock
    return new_stock


# --- Member 4 ---------------------------------------------------------------
def list_low_stock(
    inventory: Inventory, threshold: int = 5
) -> list[tuple[str, str, int]]:
    """List products with `threshold` units or fewer.
    Args:
        inventory: Inventory to check.
        threshold: Maximum stock considered low (default 5).
    Returns:
        (code, name, stock) tuples sorted by code.
    Example:
        >>> inv = {"A1": {"name": "Notebook", "price": 2.5, "stock": 4}}
        >>> list_low_stock(inv, 5)
        [('A1', 'Notebook', 4)]
    """
    low = [
        (code, product["name"], product["stock"])
        for code, product in inventory.items()
        if product["stock"] <= threshold
    ]
    return sorted(low)


# --- Member 5 ---------------------------------------------------------------
def calculate_inventory_value(inventory: Inventory) -> float:
    """Total value of the stock in EUR (sum of price * stock), 2 decimals.
    Args:
        inventory: Inventory to evaluate.
    Returns:
        The total value.
    Example:
        >>> inv = {"A1": {"name": "Notebook", "price": 2.5, "stock": 4}}
        >>> calculate_inventory_value(inv)
        10.0
    """
    total = sum(p["price"] * p["stock"] for p in inventory.values())
    return round(total, 2)


if __name__ == "__main__":
    shop: Inventory = {}
    add_product(shop, "A1", "Notebook", 2.50, 40)
    add_product(shop, "B2", "Pen", 0.80, 3)
    add_product(shop, "C3", "Backpack", 24.90, 5)

    print("Search 'pen':", search_products(shop, "pen"))
    print("Pen stock after delivery:", update_stock(shop, "B2", 20))
    print("Notebook stock after sales:", update_stock(shop, "A1", -35))
    print("Low stock (<= 5):", list_low_stock(shop, 5))
    print("Inventory value:", calculate_inventory_value(shop), "EUR")
