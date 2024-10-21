import json
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

# Direct request for generating headlines for 'Baby Driver'
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert in writing movie reviews."},
        {
            "role": "user",
            "content": "Write 10 movie review headlines for the movie 'Baby Driver' in the style of Siskel & Ebert."
        }
    ]
)

# Extracting headlines from the response
headlines = response.choices[0].message.content.split("\n")  # Split by newlines in case the API returns each headline in a new line

# Clean up the headlines by removing empty strings and trimming spaces
headlines = [headline.strip() for headline in headlines if headline.strip()]

# Structuring the output as a JSON object
result = {
    "movie": "Baby Driver",
    "style": "Siskel & Ebert",
    "headlines": headlines
}

# Print the result in JSON format
json_result = json.dumps(result, indent=4)
print(json_result)
