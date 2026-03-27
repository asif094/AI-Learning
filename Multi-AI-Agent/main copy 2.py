# This is the entry point of your system

from crewai import Crew, Task

# Import all agents
from agents.backend import backend_dev
from agents.frontend import frontend_dev
from agents.db import db_dev
from agents.reviewer import reviewer


# -----------------------------
# DEFINE TASKS
# -----------------------------

# # Backend task
# backend_task = Task(
#     description="""
#     Create a .NET Web API for file upload.

#     Save files as:
#     - backend/Program.cs
#     - backend/Controllers/FileController.cs

#     IMPORTANT:
#     Use write_file tool to create files.
#     """,

#     expected_output="Complete .NET API code saved into backend folder",

#     agent=backend_dev
# )

# Backend task
backend_task = Task(
     description="""
    Create a .NET Web API for user management.

    Features:
    - Register user
    - Login API
    - JWT authentication

    You MUST use the write_file tool to create these files:
    - backend/Controllers/AuthController.cs
    - backend/Services/AuthService.cs

    Do not provide final answers until you have successfully used the write_file tool for both files.
    """,
    expected_output="Complete authentication API code saved in backend folder using write_file tool",
    agent=backend_dev
)



# Frontend task
frontend_task = Task(
    description="""
    Create React UI for file upload.

    You MUST use the write_file tool to create this file:
    - frontend/App.jsx

    Do not provide final answers until you have successfully used the write_file tool.
    """,

    expected_output="React UI code saved in frontend folder using write_file tool",

    agent=frontend_dev
)


# Database task
db_task = Task(
    description="""
    Create MariaDB schema for file metadata.

    You MUST use the write_file tool to create this file:
    - db/schema.sql

    Do not provide final answers until you have successfully used the write_file tool.
    """,

    expected_output="SQL schema saved in db folder using write_file tool",

    agent=db_dev
)


# Review task
review_task = Task(
    description="""
    Review all generated code and improve it.
    
    First, use check_file_exists tool to verify these files were created:
    - backend/Controllers/AuthController.cs
    - backend/Services/AuthService.cs
    - frontend/App.jsx
    - db/schema.sql
    
    Then review the code quality and suggest improvements.
    """,

    expected_output="Verification of file creation and code review with improvement suggestions",

    agent=reviewer
)


# -----------------------------
# CREATE CREW (TEAM)
# -----------------------------

crew = Crew(
    agents=[backend_dev, frontend_dev, db_dev, reviewer],  # team members
    tasks=[backend_task, frontend_task, db_task, review_task],  # tasks to execute

    verbose=True  # show detailed logs
)


# -----------------------------
# RUN SYSTEM
# -----------------------------

if __name__ == "__main__":
    print("🚀 Starting Multi-Agent System...\n")

    crew.kickoff()  # start execution

    print("\n✅ Execution Completed!")