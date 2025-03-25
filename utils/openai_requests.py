import os
import openai

def check_exchange_rate(historical_exchange_rate_buy):

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

    if not OPENAI_API_KEY:
        return "Insights are not available today."

    client = openai.OpenAI(api_key=OPENAI_API_KEY) 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Please analyze the latest news of exchange rate in Costa Rica "
        "and provide somehighlights. This will embedded in HTML so please use <p> and embedded subtitles in bold. "
        "Don't include anything other than <p> and <b> tags. "
        "Please do it in one or 2 paragraphs and don't use bullet points. "
        "Here is some information of the last month: " + str(historical_exchange_rate_buy)}]
    )
    
    return response.choices[0].message.content

def banks_insights(banks_data):

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")    

    if not OPENAI_API_KEY:
        return "Insights are not available today."

    client = openai.OpenAI(api_key=OPENAI_API_KEY) 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": " Use <p> and <b> tags in the answer. Please do it in one or 2 paragraphs and don't use bullet points."
        "Choose the top three entities and analyze their values. Also choose the two with least favorable offer."
        "Who has the best exchange rate and what is your recommendation to tourists and people who most of their income is"
        " in USD. Here is a dictionary of the data for all banks: " + str(banks_data)}]
    )
    
    return response.choices[0].message.content
