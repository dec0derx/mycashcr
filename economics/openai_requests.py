<<<<<<< HEAD
import os
import openai

def check_exchange_rate(historical_exchange_rate_buy):

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    print(OPENAI_API_KEY)
    

    if not OPENAI_API_KEY:
        return "Insights are not available today."


    client = openai.OpenAI(api_key=OPENAI_API_KEY) 
=======
import openai

def check_exchange_rate(historical_exchange_rate_buy):
    client = openai.OpenAI(api_key="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")  # Replace with your actual API key
>>>>>>> 4c70642439bee050c1ff6c410ad749fd9ebf45c8

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Please analyze the trends in the exchange rate. This will embedded in HTML so please use <p> and embedded subtitles in bold. Don't include anything other than <p> and <b> tags. " + str(historical_exchange_rate_buy)}]
    )
    
    return response.choices[0].message.content

