import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file

load_dotenv()
def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    verbose_flag = False

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read the content of a file
- Write to a Python file (create or update)
- Run a specified Python file with optional arguments

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    if len(sys.argv) < 2:
        print('I need a prompt')
        sys.exit(1)

    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        verbose_flag = True
        
    prompt = sys.argv[1]

    messages = [
        types.Content(role='user', parts=[types.Part(text=prompt)]),
    ]

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents = messages, 
            config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
            )
        )
    except Exception as e:
        print(e)
        return

    if response is None or response.usage_metadata is None:
        print('response is malformed')
        return
    
    if verbose_flag:
        print(f'User prompt: {prompt}')
        print(f'Prompt Tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response Tokens: {response.usage_metadata.candidates_token_count}')

    if response.function_calls: #print out functions used, if any
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else: #no functions used
        print(response.text)
    
    


main()