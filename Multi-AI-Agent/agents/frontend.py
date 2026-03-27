from crewai import Agent
from config import llm
from tools.file_tools import write_file

frontend_dev = Agent(
    role="Frontend Developer",
    goal="Build React UI and save code into files using the write_file tool",
    backstory="Expert in React, UI/UX, API integration. Always uses tools to create files.",

    llm=llm,
    tools=[write_file],  # same tool

    verbose=True,
    allow_delegation=False
)