import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from ai-agent!")
    client = genai.Client(api_key=api_key)
    model="gemini-2.0-flash-001"
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model=model, contents=contents)
    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

if __name__ == "__main__":
    main()




