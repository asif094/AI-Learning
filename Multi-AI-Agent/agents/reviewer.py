from crewai import Agent
from config import llm
from tools.file_tools import check_file_exists

# Reviewer does not need file tool (optional)
reviewer = Agent(
    role="Code Reviewer",
    goal="Review and improve code quality, verify files were created correctly",
    backstory="Senior engineer ensuring best practices and validating deliverables",

    llm=llm,
    tools=[check_file_exists],  # Can check if files exist

    verbose=True,
    allow_delegation=False
)