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
# Create a pizza as a dictionary
my_cart = {}


# TOOL:
# Pizza management with dictionary (no class)



# AGENT:
root_agent = Agent(
    # SMALL LLM:

    model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:latest")),
    #model=LiteLlm(model="openai/"+os.environ.get("MODEL_RUNNER_MODEL", "ai/qwen2.5:1.5B-F16")),

    name="bill_agent",
    description=(
        """
        Bill agent is responsible for managing the shopping cart in a mall.
        """
    ),
    instruction="""
    You are Bill, a mall agent responsible for managing the shopping cart.
    You can search for products by name or ID.
    You can add products to the cart with their quantity.
    You can display the current cart content with quantities, prices, and total cost.
    """, 
    # TOOLS CATALOG:
    tools=[
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
