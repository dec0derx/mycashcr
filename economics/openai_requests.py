import os
import openai

def check_exchange_rate(historical_exchange_rate_buy):

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

    if not OPENAI_API_KEY:
        return "Insights are not available today."

    client = openai.OpenAI(api_key=OPENAI_API_KEY) 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Please analyze the trends in the exchange rate. This will embedded in HTML so please use <p> and embedded subtitles in bold. Don't include anything other than <p> and <b> tags. " + str(historical_exchange_rate_buy)}]
    )
    
    return response.choices[0].message.content

