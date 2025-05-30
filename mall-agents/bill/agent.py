import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
# DATA:
from .products_data import products

# SETTINGS:
os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"


# CONTENT:
# Create a shopping cart as a dictionary
my_cart = {}


# TOOL: Search products by name or name prefix
def search_product_by_name(name: str):
    """
    Search for products that contain the given name (case-insensitive)
    Args:
        name (str): The name or partial name of the product to search for
    Returns:
        dict: A dictionary of matching products with their details, or an empty dictionary if no matches
    """
    name = name.lower().strip()
    matches = {}
    
    for product_id, product_info in products.items():
        product_name = product_info['name'].lower()
        if name in product_name:
            matches[product_id] = product_info
    
    if not matches:
        print(f"No products found containing '{name}'")
        return {}
    
    print(f"Found {len(matches)} product(s) matching '{name}':")
    for product_id, info in matches.items():
        print(f"  {product_id}: {info['name']} - ${info['price']:.2f} ({info['stock']} in stock)")
    
    return matches


# TOOL: Search products by category
def search_product_by_category(category: str):
    """
    Search for products by category
    Args:
        category (str): The category to search for (electronics, clothing, books, home, sports)
    Returns:
        dict: A dictionary of products in the specified category, or an empty dictionary if category not found
    """
    category = category.lower().strip()
    valid_categories = ["electronics", "clothing", "books", "home", "sports"]
    
    if category not in valid_categories:
        print(f"Invalid category '{category}'. Valid categories are: {', '.join(valid_categories)}")
        return {}
    
    matches = {}
    
    for product_id, product_info in products.items():
        if product_info['category'] == category:
            matches[product_id] = product_info
    
    print(f"Found {len(matches)} product(s) in category '{category}':")
    for product_id, info in matches.items():
        print(f"  {product_id}: {info['name']} - ${info['price']:.2f} ({info['stock']} in stock)")
    
    return matches


# TOOL: Get product details by ID
def get_product_by_id(product_id: str):
    """
    Get detailed information about a specific product by its ID
    Args:
        product_id (str): The product ID (e.g., 'e001', 'c005', 'b003')
    Returns:
        dict: Product information if found, None if not found
    """
    product_id = product_id.lower().strip()
    
    if product_id not in products:
        print(f"Product ID '{product_id}' not found")
        return None
    
    product_info = products[product_id]
    print(f"Product Details:")
    print(f"  ID: {product_id}")
    print(f"  Name: {product_info['name']}")
    print(f"  Description: {product_info['description']}")
    print(f"  Price: ${product_info['price']:.2f}")
    print(f"  Category: {product_info['category']}")
    print(f"  Stock: {product_info['stock']} units")
    
    return product_info


# TOOL: Advanced search combining name and category
def search_products_advanced(name: str = "", category: str = ""):
    """
    Advanced search that can filter by both name and category
    Args:
        name (str, optional): Name or partial name to search for
        category (str, optional): Category to filter by
    Returns:
        dict: Dictionary of matching products
    """
    matches = {}
    name = name.lower().strip() if name else ""
    category = category.lower().strip() if category else ""
    
    for product_id, product_info in products.items():
        # Check name match
        name_match = not name or name in product_info['name'].lower()
        
        # Check category match
        category_match = not category or product_info['category'] == category
        
        # Include if both conditions are met
        if name_match and category_match:
            matches[product_id] = product_info
    
    if not matches:
        search_criteria = []
        if name:
            search_criteria.append(f"name containing '{name}'")
        if category:
            search_criteria.append(f"category '{category}'")
        print(f"No products found with {' and '.join(search_criteria)}")
        return {}
    
    print(f"Found {len(matches)} product(s):")
    for product_id, info in matches.items():
        print(f"  {product_id}: {info['name']} - ${info['price']:.2f} ({info['category']}) - {info['stock']} in stock")
    
    return matches


# TOOL: Add product to cart
def add_to_cart(product_id: str, quantity: int = 1):
    """
    Add a product to the shopping cart
    Args:
        product_id (str): The product ID to add
        quantity (int): Quantity to add (default: 1)
    Returns:
        bool: True if successful, False if product not found or insufficient stock
    """
    product_id = product_id.lower().strip()
    
    if quantity is None or quantity <= 0:
        quantity = 1
    
    if product_id not in products:
        print(f"Product ID '{product_id}' not found")
        return False
    
    product_info = products[product_id]
    
    # Check stock availability
    if product_info['stock'] < quantity:
        print(f"Insufficient stock. Only {product_info['stock']} units available")
        return False
    
    # Add to cart or update existing quantity
    if product_id in my_cart:
        my_cart[product_id]['quantity'] += quantity
    else:
        my_cart[product_id] = {
            'name': product_info['name'],
            'price': product_info['price'],
            'quantity': quantity
        }
    
    print(f"Added {quantity} x {product_info['name']} to cart")
    return True


# TOOL: Display cart contents
def display_cart():
    """
    Display the current shopping cart contents with total cost
    Returns:
        str: Formatted string showing cart contents and total price
    """
    if not my_cart:
        return "Your shopping cart is empty!"
    
    result = "SHOPPING CART CONTENTS\n"
    result += "=" * 50 + "\n"
    
    total_cost = 0.0
    total_items = 0
    
    for product_id, cart_item in my_cart.items():
        item_total = cart_item['price'] * cart_item['quantity']
        result += f"• {cart_item['name']}: "
        result += f"{cart_item['quantity']} unit(s) × ${cart_item['price']:.2f} = ${item_total:.2f}\n"
        total_cost += item_total
        total_items += cart_item['quantity']
    
    result += "=" * 50
    result += f"\n**TOTAL ITEMS: {total_items}**"
    result += f"\n**TOTAL COST: ${total_cost:.2f}**"
    
    return result

# TOOL: Remove item from cart
def remove_from_cart(product_id: str, quantity: int = 0):
    """
    Remove a product from the shopping cart
    Args:
        product_id (str): The product ID to remove
        quantity (int): Quantity to remove. If 0 or negative, removes all items of this product
    Returns:
        bool: True if successful, False if product not found in cart
    """
    product_id = product_id.lower().strip()
    
    if product_id not in my_cart:
        print(f"Product ID '{product_id}' not found in cart")
        return False
    
    cart_item = my_cart[product_id]
    current_quantity = cart_item['quantity']
    
    # If quantity is 0 or negative, or quantity >= current quantity, remove all
    if quantity <= 0 or quantity >= current_quantity:
        removed_quantity = current_quantity
        del my_cart[product_id]
        print(f"Removed all {removed_quantity} x {cart_item['name']} from cart")
    else:
        # Remove specified quantity
        my_cart[product_id]['quantity'] -= quantity
        print(f"Removed {quantity} x {cart_item['name']} from cart ({my_cart[product_id]['quantity']} remaining)")
    
    return True



# AGENT:
root_agent = Agent(
    # SMALL LLM:
    model=LiteLlm(model="openai/" + os.environ.get('MODEL_RUNNER_MODEL')),
    #model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:latest")),
    #model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:1.5B-F16")),

    name="bill_agent",
    description=(
        """
        Bill agent is responsible for managing the shopping cart in a mall.
        He can search for products by name, category, or ID, and manage a shopping cart.
        """
    ),
    instruction="""
    You are Bill, a helpful mall agent responsible for managing the shopping cart.
    
    You can help customers:
    - Search for products by name (partial matches work)
    - Browse products by category (electronics, clothing, books, home, sports)
    - Get detailed information about specific products using their ID
    - Add products to their shopping cart with desired quantities
    - View their current cart contents and total cost
    - Use advanced search to find products with specific criteria
    
    Available product categories:
    - electronics: phones, laptops, gadgets
    - clothing: shoes, jackets, accessories
    - books: various genres and topics
    - home: appliances, furniture, smart home items
    - sports: fitness equipment, outdoor gear
    
    Be friendly and helpful in assisting customers find what they're looking for!
    """, 
    # TOOLS CATALOG:
    tools=[
        search_product_by_name,
        search_product_by_category,
        get_product_by_id,
        search_products_advanced,
        add_to_cart,
        display_cart,
        remove_from_cart,
        MCPToolset(
            connection_params=StdioServerParameters(
                command='socat',
                args=[
                    "STDIO",
                    "TCP:host.docker.internal:8811",
                ],
            ),
            # Optional: Filter which tools from the MCP server are exposed
            tool_filter=['brave_web_search']
        )
    ],
)