import os
import shlex
import subprocess
import sys
from functions import config

def run_python_file(working_directory, file_path, args=[]):
    output=""

    path=os.path.join(working_directory, file_path)

    if ".." in file_path or not working_directory in path:
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    if not os.path.exists(path):
        return (f'Error: File "{file_path}" not found.')
    
    if not file_path.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file.')
    
    try:
        command=["uv","run",file_path] + list(args)
        completed_process=subprocess.run(command, timeout=30, capture_output=True, text=True, cwd=working_directory)
        stdout=completed_process.stdout.strip()
        stderr=completed_process.stderr.strip()
        return_code=completed_process.returncode
        if stdout=="" and stderr=="":
            output=output + "No output produced.\n"
        else:
            output=output+"STDOUT: "+stdout+"\n"
            output=output+"STDERR: "+stderr+"\n"
        if return_code!=0:
            output=output + f'Process exited with code {return_code}\n'
    except Exception as e:
        return (f"Error: executing Python file: {e}")
    
    else:
        return (output)



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

    # Use the subprocess.run function to execute the Python file and get back a "completed_process" object. Make sure to:
    # Set a timeout of 30 seconds to prevent infinite execution
    # Capture both stdout and stderr
    # Set the working directory properly
    # Pass along the additional args if provided
    # Return a string with the output formatted to include:
    # The stdout prefixed with STDOUT:, and stderr prefixed with STDERR:. The "completed_process" object has a stdout and stderr attribute.
    # If the process exits with a non-zero code, include "Process exited with code X"
    # If no output is produced, return "No output produced."
    # If any exceptions occur during execution, catch them and return an error string: