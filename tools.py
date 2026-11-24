import pandas as pd
from smolagents import tool

PRODUCTS_PATH = "data/products.csv"
ORDERS_PATH = "data/orders.csv"

@tool
def list_products(category: str = "") -> str:
    """List all makeup products or filter by category (lipstick, foundation, primer, concealer, cleanser, setting_spray).

    Args:
        category: Optional category filter. Leave empty to list all.
    """
    df = pd.read_csv(PRODUCTS_PATH)
    if category:
        df = df[df["category"].str.lower() == category.lower()]
    if df.empty:
        return "No products found in that category."
    lines = []
    for _, row in df.iterrows():
        lines.append(f"{row['name']} (ID:{row['id']}) - ¥{row['price']}, stock: {row['stock']}, skin: {row['skin_type']}")
    return "\n".join(lines)

@tool
def check_stock(product_name: str) -> str:
    """Check the stock availability of a specific product.

    Args:
        product_name: Name of the product to check.
    """
    df = pd.read_csv(PRODUCTS_PATH)
    match = df[df["name"].str.lower().str.contains(product_name.lower())]
    if match.empty:
        return f"Product '{product_name}' not found."
    row = match.iloc[0]
    return f"{row['name']}: stock {row['stock']}, price ¥{row['price']}."

@tool
def recommend_by_skin(skin_type: str) -> str:
    """Recommend makeup products suitable for a given skin type (dry, oily, sensitive, all).

    Args:
        skin_type: The user's skin type.
    """
    df = pd.read_csv(PRODUCTS_PATH)
    df = df[(df["skin_type"].str.lower() == skin_type.lower()) | (df["skin_type"] == "all")]
    df = df[df["stock"] > 0]
    if df.empty:
        return f"No in-stock products suitable for {skin_type} skin."
    return "\n".join(f"{row['name']} - ¥{row['price']}" for _, row in df.iterrows())

@tool
def place_order(product_name: str, quantity: int) -> str:
    """Place an order for a product and save it to orders.csv.

    Args:
        product_name: Name of the product to order.
        quantity: Number of units.
    """
    products = pd.read_csv(PRODUCTS_PATH)
    match = products[products["name"].str.lower().str.contains(product_name.lower())]
    if match.empty:
        return f"Product '{product_name}' not found."
    idx = match.index[0]
    row = products.loc[idx]
    if row["stock"] < quantity:
        return f"Sorry, only {row['stock']} units of {row['name']} left."
    # Update stock
    products.loc[idx, "stock"] = row["stock"] - quantity
    products.to_csv(PRODUCTS_PATH, index=False)
    # Save order
    orders = pd.read_csv(ORDERS_PATH)
    new_id = len(orders) + 1
    new_order = pd.DataFrame([{
        "order_id": new_id,
        "product_id": row["id"],
        "product_name": row["name"],
        "quantity": quantity,
        "total_price": row["price"] * quantity
    }])
    orders = pd.concat([orders, new_order], ignore_index=True)
    orders.to_csv(ORDERS_PATH, index=False)
    return f"Order placed: {quantity} x {row['name']}, total ¥{row['price'] * quantity}."