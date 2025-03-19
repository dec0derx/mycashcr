import os
import openai

def check_exchange_rate(historical_exchange_rate_buy):

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

    if not OPENAI_API_KEY:
        return "Insights are not available today."

    client = openai.OpenAI(api_key=OPENAI_API_KEY) 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Please analyze the latest news of exchange rate in Costa Rica and provide somehighlights. This will embedded in HTML so please use <p> and embedded subtitles in bold. Don't include anything other than <p> and <b> tags. Here is some information of the last month: " + str(historical_exchange_rate_buy)}]
    )
    
    return response.choices[0].message.content

def banks_insights(banks_data):

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

    if not OPENAI_API_KEY:
        return "Insights are not available today."

    client = openai.OpenAI(api_key=OPENAI_API_KEY) 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": " Use <p> and <b> tags in the answer. The first value is the buy rate in the bank and the second one is the sell value. Who has the best exchange rate and what is your recommendation to tourists (use the value to the left - highest is better)? Here is a dictionary of the data for all banks: " + str(banks_data)}]
    )
    
    return response.choices[0].message.content
