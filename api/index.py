from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def main():
    user_query = input("Enter your query: ")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_query}  
        ]
    )
    
    print("Response:", response.choices[0].message.content)
    
main()