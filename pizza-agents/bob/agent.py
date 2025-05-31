import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
# DATA:
# Import the externalized pizza data
from .pizza_data import pizza_ingredients

# SETTINGS:
os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"


# CONTENT:
# Create a pizza as a dictionary
my_pizza = {}


# TOOL:
# Pizza management with dictionary (no class)
def add_ingredient(name :str, quantity: int):
    """
    Add an ingredient with the specified name and quantity to the pizza dictionary
    Args:
        name (str): The name of the ingredient
        quantity (int): The quantity of the ingredient to add
    Returns:
        bool: True if successful, False if ingredient not found
    """
    # test if quantity is null or 0
    if quantity is None or quantity <= 0:
        quantity = 1

    name = name.lower().strip()
    
    # Check if ingredient exists in our dictionary
    if name not in pizza_ingredients:
        print(f"Error: '{name}' not found in ingredients list")
        return False
    
    unit_price = pizza_ingredients[name]
    total_price = unit_price * quantity
    
    # If ingredient already exists, add to existing quantity
    if name in my_pizza:
        old_quantity = my_pizza[name]['quantity']
        new_quantity = old_quantity + quantity
        my_pizza[name] = {
            'quantity': new_quantity,
            'unit_price': unit_price,
            'total_price': unit_price * new_quantity
        }
        print(f"Added {quantity} more {name} (total: {new_quantity})")
    else:
        my_pizza[name] = {
            'quantity': quantity,
            'unit_price': unit_price,
            'total_price': total_price
        }
        print(f"Added {quantity} {name}")

# TOOL:
def display_pizza_content():
    """
    Display the current content of the pizza with quantities, prices, and total cost
    Returns:
        str: Formatted string showing pizza contents and total price
    """
    if not my_pizza:
        return "Your pizza is empty! No ingredients added yet."
    
    result = "CURRENT PIZZA CONTENTS\n"
    result += "=" * 40 + "\n"
    
    total_cost = 0.0
    
    for ingredient, data in my_pizza.items():
        result += f"• {ingredient.replace('_', ' ').title()}: "
        result += f"{data['quantity']} unit(s) × ${data['unit_price']:.2f} = ${data['total_price']:.2f}\n"
        total_cost += data['total_price']
    
    result += "=" * 40
    result += f"\n**TOTAL COST: ${total_cost:.2f}**"
    result += f"\n**INGREDIENTS: {len(my_pizza)} types**"
    
    return result


# TOOL:
# Function to search ingredients by name
def search_ingredient_by_name(name: str):
    """
    Search for ingredients that start with the given name
    Args:
        name (str): The name or prefix of the ingredient
    Returns:
        dict: A dictionary of matching ingredients and their prices, or an empty dictionary if no matches are found
    """
    name = name.lower().strip()
    matches = {ingredient: price for ingredient, price in pizza_ingredients.items() if ingredient.startswith(name)}
    
    if not matches:
        print(f"No ingredients found starting with '{name}'")
        return {}
    
    return matches


# AGENT:
root_agent = Agent(
    # SMALL LLM:
    model=LiteLlm(model="openai/" + os.environ.get('MODEL_RUNNER_MODEL')),
    #model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:latest")),
    #model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:latest")),
    #model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:1.5B-F16")),

    name="bob_agent",
    description=(
        """
        Bob agent is a pizza expert.
        """
    ),
    instruction="""
    You are Bob, a pizza expert. 
    Use the tools provided to interact with users.
    You can search for ingredients by name.
    You can add ingredients and quantity to a pizza.
    You can display the current pizza content with quantities, prices, and total cost.
    """,
    # TOOLS CATALOG:
    tools=[
        search_ingredient_by_name,
        add_ingredient,
        display_pizza_content,
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
