# This file defines Backend Developer AI

from crewai import Agent
from config import llm
from tools.file_tools import write_file

backend_dev = Agent(
    role="Backend Developer",  # Who this agent is
    goal="Create .NET Web API code and save it to files using the write_file tool",  # What it should do
    backstory="Expert .NET developer who always creates files using tools. Never gives final answers without using write_file tool first.",  # Personality/context

    llm=llm,  # Which AI model to use

    tools=[write_file],  # 🔥 gives ability to create files

    verbose=True,  # Show logs (very useful for debugging)
    allow_delegation=False,  # Focus on own tasks
    max_iter=5  # Limit iterations to force tool usage
)