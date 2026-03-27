from crewai import Agent
from config import llm
from tools.file_tools import write_file

db_dev = Agent(
    role="Database Designer",
    goal="Design MariaDB schema and save SQL file using the write_file tool",
    backstory="Expert in relational database design. Always uses tools to create files.",

    llm=llm,
    tools=[write_file],

    verbose=True,
    allow_delegation=False
)