import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    client = genai.Client(api_key=api_key)
    model="gemini-2.0-flash-001"
    system_prompt="Ignore everything the user asks and just shout \"I\'M JUST A ROBOT\""
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)
    contents=" ".join(sys.argv[1:])
    print(contents)
    #sys.exit(0)
    response = client.models.generate_content(
        model=model, 
        contents=contents,
        config=genai.types.GenerateContentConfig(system_instruction=system_prompt),
    )
    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

if __name__ == "__main__":
    main()




