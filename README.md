# Store Inventory

A small Python inventory manager for a shop. You can add products, search for them, update the stock, see which products are running out and calculate the value of the stock.

## How to run

```bash
python store_inventory.py            # demo
python -m doctest store_inventory.py # run the docstring examples
```

## Example

```
Search 'pen': [('B2', {'name': 'Pen', 'price': 0.8, 'stock': 3})]
Pen stock after delivery: 23
Notebook stock after sales: 5
Low stock (<= 5): [('A1', 'Notebook', 5), ('C3', 'Backpack', 5)]
Inventory value: 155.4 EUR
```

## Functions

| Function | What it does | Author |
|---|---|---|
| `add_product` | Adds a new product | Alvaro |
| `search_products` | Finds products by code or name | Otto |
| `update_stock` | Adds or removes items from the stock | Althay |
| `list_low_stock` | Shows products that are running out | Pablo |
| `calculate_inventory_value` | Calculates the value of the stock | Ángel |

## License

MIT. See the [LICENSE](LICENSE) file.
