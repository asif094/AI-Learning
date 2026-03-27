# This file connects CrewAI to your local Ollama model

from crewai import LLM

# Create LLM object
# This tells CrewAI:
# → Use Ollama
# → Use deepseek-coder model
# → Connect to local server (default Ollama port)

llm = LLM(
    model="ollama/deepseek-coder",
    base_url="http://localhost:11434",
    api_key="ollama",  # required for LiteLLM compatibility
    timeout=1200   # increase timeout (20 min)
)