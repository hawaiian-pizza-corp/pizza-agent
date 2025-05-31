import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse, LlmRequest
from typing import Optional, List
#from google.genai import types # For types.Content


from litellm import embedding
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document

# DOCUMENTS:
from .documents import star_trek_docs

# NOTE: this will be triggered at the first request to the agent

# SETTINGS:
os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

print("🟡 Initialize...")

# HELPER: LiteLLM Embedding Wrapper (custom embedding class)
class LiteLLMEmbeddingWrapper(Embeddings):
    def __init__(self):
        self.model = "openai/" + os.environ.get('MODEL_RUNNER_EMBEDDING_MODEL')
        self.api_base = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        response = embedding(
            model=self.model,
            api_key="tada",  # Your API key
            api_base=self.api_base,
            input=texts
        )
        return [e['embedding'] for e in response.data]

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]


# VECTOR STORE: Initialize vector store with your embeddings
embeddings = LiteLLMEmbeddingWrapper()
vector_store = InMemoryVectorStore(embedding=embeddings)

print("🟠 List of the documents:")
# Loop through docs and create embeddings
for document in star_trek_docs:
    print(document)
    print("-" * 50)  # separator


# DOCUMENTS: Add documents: convert star_trek_docs to Document objects
documents = [Document(page_content=text, metadata={}) for text in star_trek_docs]

# DATA: you can add them to the vector store
vector_store.add_documents(documents=documents)


# NOTE: this triggered at every request to the agent
def on_request(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("⚡️ Request received")

    return None



# TOOL:
def search_for(question: str):
    """
    Use the entire user question to search for similarities.
    Args:
        question (str): The full question asked by the user, unmodified.
    Returns:
        list: The list of similarities found.
    """

    print(f"🔎 Searching for similarities with question: {question}")

    # Perform similarity search
    results = vector_store.similarity_search(question, k=1)

    return results
 

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
    before_model_callback= on_request,
)
