# This file defines a TOOL that agents can use
# Think of it like giving "hands" to AI agents

from crewai.tools import tool
import os

# @tool decorator converts normal function → AI usable tool
@tool
def write_file(path: str, content: str) -> str:
    """
    Writes content to a file.
    
    Parameters:
    path → file location (example: backend/app.py)
    content → code/text to write
    
    Returns:
    success message
    """

    # Create folder automatically if not exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Write content to file
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File written successfully: {path}"


@tool
def check_file_exists(path: str) -> str:
    """
    Checks if a file exists at the given path.
    
    Parameters:
    path → file location to check (example: backend/app.py)
    
    Returns:
    'File exists' or 'File does not exist'
    """
    
    if os.path.exists(path):
        return f"File exists: {path}"
    else:
        return f"File does not exist: {path}"