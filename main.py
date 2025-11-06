import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info

load_dotenv()
def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    verbose_flag = False

    if len(sys.argv) < 2:
        print('I need a prompt')
        sys.exit(1)

    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        verbose_flag = True
        
    prompt = sys.argv[1]

    messages = [
        types.Content(role='user', parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents = messages,
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print('response is malformed')
        return
    if verbose_flag:
        print(f'User prompt: {prompt}')
        print(f'Prompt Tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response Tokens: {response.usage_metadata.candidates_token_count}')

main()