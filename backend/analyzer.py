# we need this line cuz python automatically won't pick up the env variable??
from dotenv import load_dotenv
import os

load_dotenv()

# load_dotenv() reads the .env file and loads gemini api into the env, letting us to what we need to do

from google import genai
from google.genai import types
client = genai.Client() # need a var to store the function don't we?

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="When did first-wave black metal start?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    )
)

print(response.text)

