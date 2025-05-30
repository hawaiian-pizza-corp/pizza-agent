import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


# SETTINGS:
os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

# TOOL:
def search_for(question: str):
    """
    Use the entire user question to search for similarities.
    Args:
        question (str): The full question asked by the user, unmodified.
    Returns:
        list: The list of similarities found.
    """
    print(f"🔴 Searching for similarities with question: {question}")
    return ["one", "two", "three"]
 

# AGENT:
root_agent = Agent(
    # SMALL LLM:
    model=LiteLlm(model="openai/" + os.environ.get('MODEL_RUNNER_MODEL')),

    name="milo_agent",
    description=(
        """
        Milo agent is a search expert.
        """
    ),
    instruction="""
    If the user asks a question, always use the 'search_for' tool with the complete user question as the parameter.
    Do not extract keywords or modify the question; always pass the full question as it was asked.
    If the 'search_for' tool returns content, use that content to answer the user.
    Example: If the user says 'Who is John Lennon?', call search_for('Who is John Lennon?').
    """,
    tools=[search_for],
)
