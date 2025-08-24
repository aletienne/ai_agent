import os


def get_files_info(working_directory, directory="."):
    output=[]
    string_output=""
    path=os.path.join(working_directory, directory)
    if directory==".":
        line="Result for current directory:"
    else:
        line=f'Result for "{directory}" directory:'
    output.append(line) 
    if ".." in directory or not working_directory in path:
        output.append("    Error: Cannot list " + directory + " as it is outside the permitted working directory")
        return ("\n".join(output))
    if not os.path.isdir(path):
        output.append(f'    Error: "{directory}" is not a directory')
        return ("\n".join(output))
    items=os.listdir(path)

    for i in items:
        file=os.path.join(path, i)
        is_dir=os.path.isdir(file)
        if is_dir:
            file_size=os.path.getsize(file)
            line=f' - {i}: file_size={file_size} bytes, is_dir={is_dir}'
        else:
            file_size=os.path.getsize(file)
            line=f' - {i}: file_size={file_size} bytes, is_dir=False'
        output.append(line)
    return ("\n".join(output))


# Result for current directory:
# - main.py: file_size=576 bytes, is_dir=False
# - tests.py: file_size=1343 bytes, is_dir=False
# - pkg: file_size=92 bytes, is_dir=True

# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator