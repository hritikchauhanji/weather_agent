from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    return "Something went wrong"

def main():
    user_query = input("Enter your query: ")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_query}  
        ]
    )
    
    print("Response:", response.choices[0].message.content)
    
# main()
print(get_weather("New York"))