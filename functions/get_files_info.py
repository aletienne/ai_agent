import os

def get_files_info(working_directory, directory="."):
    path=os.path.join(working_directory, directory)
    if ".." in directory or not working_directory in path:
        return ("Error: Cannot list " + directory + " as it is outside the permitted working directory")
    return (path)