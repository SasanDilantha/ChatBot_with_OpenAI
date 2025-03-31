import os
from openai import OpenAI  # type: ignore
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

while True:
    quaction = input("User : ")
    if quaction == "bye":
        print("AI: Bye...")
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=50,
        n=1,
        temperature=0,
        messages=[
            {"role":"user", "content":quaction}
        ]
    )

    for ans in response.choices:
        print(f"AI : {ans.message.content}")