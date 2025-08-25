import os
from functions import config

from google import genai
import google.genai
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get content from, relative to the working directory.",
            ),
        },
    ),
)


def get_file_content(working_directory, file_path):

    path=os.path.join(working_directory, file_path)

    if ".." in file_path or not working_directory in path:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    
    with open(path,"r") as f:
        file_content_string = f.read(config.file_limit)
    return file_content_string

# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator
# os.path.exists: Check if a path exists
# os.makedirs: Create a directory and all its parents
# os.path.dirname: Return the directory name