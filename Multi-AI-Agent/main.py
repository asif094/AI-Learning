from crewai import Crew, Task

from agents.backend import backend_dev
from agents.frontend import frontend_dev
from agents.db import db_dev
from agents.reviewer import reviewer


# -----------------------------
# USER INPUT (Dynamic Prompt)
# -----------------------------

print("🧠 Multi-Agent AI System")
print("Choose agent:")
print("1 - Backend Developer")
print("2 - Frontend Developer")
print("3 - Database Designer")
print("4 - Code Reviewer")

choice = input("Enter choice: ")

user_prompt = input("\nEnter your instruction:\n")


# -----------------------------
# SELECT AGENT
# -----------------------------

agent_map = {
    "1": backend_dev,
    "2": frontend_dev,
    "3": db_dev,
    "4": reviewer
}

selected_agent = agent_map.get(choice)

if not selected_agent:
    print("❌ Invalid choice")
    exit()


# -----------------------------
# CREATE TASK DYNAMICALLY
# -----------------------------

task = Task(
    description=f"""
    {user_prompt}

    IMPORTANT:
    - If code is generated, save it using write_file tool
    - Do not just explain, create real files
    """,
    expected_output="Task completed with files created if needed",
    agent=selected_agent
)


# -----------------------------
# RUN CREW
# -----------------------------

crew = Crew(
    agents=[selected_agent],
    tasks=[task],
    verbose=True
)

print("\n🚀 Running...\n")

result = crew.kickoff()

print("\n✅ RESULT:\n")
print(result)