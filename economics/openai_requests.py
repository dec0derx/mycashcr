#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

import openai

def check_exchange_rate(historical_exchange_rate_buy):
    client = openai.OpenAI(api_key="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")  # Replace with your actual API key

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Please analyze the trends in the exchange rate. This will embedded in HTML so please use <p> and embedded subtitles in bold. Don't include anything other than <p> and <b> tags. " + str(historical_exchange_rate_buy)}]
    )
    
    return response.choices[0].message.content


