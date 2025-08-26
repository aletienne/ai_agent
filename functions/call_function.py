import os
from functions import config
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

from google import genai
import google.genai
from google.genai import types

import warnings
warnings.filterwarnings("ignore")

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name=function_call_part.name
    args=function_call_part.args
    match function_name:
        case "get_files_info":
            # def get_files_info(working_directory, directory="."):
            function_result=get_files_info(config.working_directory, **args)
        case "get_file_content":
            # def get_file_content(working_directory, file_path):
            function_result=get_file_content(config.working_directory, **args)
        case "write_file":
            # def write_file(working_directory, file_path, content):
            function_result=write_file(config.working_directory, **args)
        case "run_python_file":
            # def run_python_file(working_directory, file_path, args=[]):
            function_result=run_python_file(config.working_directory, **args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
        
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )