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

"""Store Inventory: a small inventory manager for a shop."""

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
    inv = {}
    add_product(inv, "A1", "Notebook", 2.5, 40)
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
def search_product(inventory: list, product: str) -> list:
    """
    Search for a product in the inventory by name.
    Args:
        inventory (list): List of products. [product name (str), stock (int), price (float)        
        product (str): Name of the product to search for.
    Returns:
        -> list: Product information [name, stock, price]
        -> None: if the product is not in the inventory
        
    
    Example:
        inventory = [
            ["Mouse", 10, 15.0],
            ["Keyboard", 8, 30.0],
            ["Monitor", 3, 120.0]
        ]
        
        search_product(inventory, "Monitor") --> ["Monitor", 3, 120.0]
        """
    information = None  # if after the loop the product name is not found, return None
    
    for i in range(len(inventory)):
        if inventory[i][0] == product:
            information = inventory[i]
            break  # stop when we find the product
    
    return information


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
    inv = {"B2": {"name": "Pen", "price": 0.8, "stock": 3}}
    update_stock(inv, "B2", 20)
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
def list_low_stock(inventory, threshold: int = 5):
    """Returns a list of products with stock equal to or below the threshold.
    Args:
        inventory (dict): Dictionary containing the products.
        threshold (int): Maximum stock to be considered low.
    Returns:
        list: Products with their code, name and stock.
    Example:
        list_low_stock(inventory)
        [('A1', 'Notebook', 4)]
    """
    low_stock = []  # List to store products with low stock
    for product_code in inventory:
        product = inventory[product_code]  # Get product information
        if product["stock"] <= threshold:  # Check if stock is lower than te threshold
            low_stock.append((product_code, product["name"], product["stock"]))
    return sorted(low_stock)  # Return the list sorted by product code


# --- Member 5: Ángel Alfonso Arteaga Romero ----------------------------------
def total_value(inventory: Inventory) -> float:
    """Calculate the total monetary value of all products in the inventory.
    Args:
        inventory: Inventory mapping product codes to their details.
    Returns:
        The total value as a float.
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
    return sum(product["price"] * product["stock"] for product in inventory.values())


if __name__ == "__main__":
    # Example inventory (from list_low_stock)
    inventory = {
        "A1": {"name": "Notebook", "price": 2.5, "stock": 4},
        "A2": {"name": "Pencil", "price": 1.0, "stock": 10}
    }
    # Print products with low stock
    print(list_low_stock(inventory))

    # Demo of the other functions
    add_product(inventory, "B2", "Pen", 0.80, 3)
    print("Pen stock after delivery:", update_stock(inventory, "B2", 20))
    print("Inventory value:", total_value(inventory), "EUR")

    # search_product works with a list of lists, not with the dictionary
    products = [["Mouse", 10, 15.0], ["Keyboard", 8, 30.0], ["Monitor", 3, 120.0]]
    print("Search 'Monitor':", search_product(products, "Monitor"))
