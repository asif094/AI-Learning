from crewai import Crew, Task

from agents.backend import backend_dev
from agents.frontend import frontend_dev
from agents.db import db_dev
from agents.reviewer import reviewer

# Define Tasks

# backend_task = Task(
#     description="Create .NET Web API for file upload with endpoints",
#     expected_output="Complete .NET API code with controllers and endpoints",
#     agent=backend_dev
# )

backend_task = Task(
    description="""
    Create a .NET Web API for file upload.

    Save files as:
    - backend/Controllers/FileController.cs
    - backend/Program.cs

    Use write_file tool to save files.
    """,
    expected_output="Complete .NET API code saved into backend folder",
    agent=backend_dev
)

frontend_task = Task(
    description="Create React UI to upload file and call API",
    expected_output="React components with file upload UI and API integration",
    agent=frontend_dev
)

db_task = Task(
    description="Design MariaDB table to store file metadata",
    expected_output="SQL schema with table structure for file metadata",
    agent=db_dev
)

review_task = Task(
    description="Review all generated code and improve it",
    expected_output="Improved and optimized version of code with suggestions",
    agent=reviewer
)

# Create Crew
crew = Crew(
    agents=[backend_dev, frontend_dev, db_dev, reviewer],
    tasks=[backend_task, frontend_task, db_task, review_task],
    verbose=True
)

# Run system
if __name__ == "__main__":
    crew.kickoff()