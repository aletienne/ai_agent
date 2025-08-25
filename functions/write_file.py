import os
from functions import config

from google import genai
import google.genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the contents of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):

    path=os.path.join(working_directory, file_path)

    if ".." in file_path or not working_directory in path:
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    try:
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

    except Exception as e:
        return (f'Error: Could not write to file "{file_path}". Exception: {str(e)}')
    
    else:
        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator
#
# os.path.exists: Check if a path exists
# os.makedirs: Create a directory and all its parents
# os.path.dirname: Return the directory name