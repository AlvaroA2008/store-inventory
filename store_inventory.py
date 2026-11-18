# MIT License
#
# Copyright (c) 2026 Álvaro Antonio Sánchez Suárez, Otto Sánchez-Tembleque Meneses, Althay Sánchez González, Pablo Alexander Hernández García, Ángel Alfonso Arteaga Romero
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

All functions use the same inventory format, a dictionary:
    {"A1": {"name": "Notebook", "price": 2.5, "stock": 4}, ...}
"""

Inventory = dict[str, dict[str, str | float | int]]


# --- Member 1: Álvaro Antonio Sánchez Suárez ---------------------------------
def add_product(inventory: Inventory, code: str, name: str, price: float, stock: int) -> dict:
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


# --- Member 2: Otto Sánchez-Tembleque Meneses --------------------------------
def search_product(inventory: Inventory, product: str) -> dict | None:
    """Search for a product in the inventory by name (ignores capital letters).
    Args:
        inventory: Inventory mapping product codes to their details.
        product: Name of the product to search for.
    Returns:
        The product details as a dict, or None if the product is not in the inventory.
    Example:
        >>> inv = {"B2": {"name": "Pen", "price": 0.8, "stock": 3}}
        >>> search_product(inv, "pen")
        {'name': 'Pen', 'price': 0.8, 'stock': 3}
    """
    
    for code in inventory:
        if inventory[code]["name"].lower() == product.strip().lower():
            return inventory[code]
    return None  # return None if the product name is not found


# --- Member 3: Althay Sánchez González ---------------------------------------
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


# --- Member 4: Pablo Alexander Hernández García ------------------------------
def list_low_stock(inventory: Inventory, threshold: int = 5) -> list[tuple[str, str, int]]:
    """Return the products with stock equal to or below the threshold.
    Args:
        inventory: Inventory mapping product codes to their details.
        threshold: Maximum stock to be considered low (default 5).
    Returns:
        List of (code, name, stock) tuples, sorted by product code.
    Example:
        >>> inv = {"A1": {"name": "Notebook", "price": 2.5, "stock": 4}}
        >>> list_low_stock(inv)
        [('A1', 'Notebook', 4)]
    """
    low_stock = []  # List to store products with low stock
    for product_code in inventory:
        product = inventory[product_code]  # Get product information
        if product["stock"] <= threshold:  # Check if stock is lower than the threshold
            low_stock.append((product_code, product["name"], product["stock"]))
    return sorted(low_stock)  # Return the list sorted by product code


# --- Member 5: Ángel Alfonso Arteaga Romero ----------------------------------
def total_value(inventory: Inventory) -> float:
    """Calculate the total monetary value of all products in the inventory.
    Args:
        inventory: Inventory mapping product codes to their details.
    Returns:
        The total value as a float, rounded to 2 decimals.
    Example:
        >>> inv = {
        ...     "A1": {"name": "Apples", "price": 2.0, "stock": 10},
        ...     "B2": {"name": "Bread", "price": 3.5, "stock": 4},
        ... }
        >>> total_value(inv)
        34.0
    """
    # Loop through each product's details (ignoring the product codes),
    # multiply its price by its stock, and add all results together
    total = sum(product["price"] * product["stock"] for product in inventory.values())
    return round(total, 2)


if __name__ == "__main__":
    # Example inventory: every function uses the same dictionary
    inventory: Inventory = {}
    add_product(inventory, "A1", "Notebook", 2.5, 4)
    add_product(inventory, "A2", "Pencil", 1.0, 10)
    add_product(inventory, "B2", "Pen", 0.8, 3)

    print("Search 'pen':", search_product(inventory, "pen"))
    print("Pen stock after delivery:", update_stock(inventory, "B2", 20))
    print("Low stock (<= 5):", list_low_stock(inventory))
    print("Inventory value:", total_value(inventory), "EUR")
