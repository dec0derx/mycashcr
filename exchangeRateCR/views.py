from django.shortcuts import render
from django.utils import timezone

import requests
from bs4 import BeautifulSoup
from utils import openai_requests
from .models import BanksInsight


# Create your views here.

def exchange_rate(request):
    banks_exchange_rate_dictionary = get_commercial_banks_exchange_rate()

    header = ["Institution", "Buy Rate", "Sell Rate"]

    # Insert the header at the beginning of the list
    banks_exchange_rate_dictionary.insert(0, header)

    current_date = timezone.now().date()

    # Query the ExchangeRateSummary model by the current date
    insights = BanksInsight.objects.filter(date=current_date).first()

    # If no summary exists for the current date, create a new one
    if not insights:
        insights_text = openai_requests.banks_insights(banks_exchange_rate_dictionary)
        insights = BanksInsight.objects.create(insight=insights_text)
    else:
        insights_text = insights.insight

    banks_exchange_rate_dictionary.remove(header)
    print("\n")

    args = {'banks_exchange_rate_dictionary': banks_exchange_rate_dictionary,
            'banks_data_sumary': insights_text}
    return render(request, "exchangeRateCR/exchange_rate.html", args)

def get_commercial_banks_exchange_rate():
    URL = "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx"
    page = requests.get(URL)

    html_content = BeautifulSoup(page.content, "html.parser")

    entities_table = html_content.find('table', id="DG")
    rows = entities_table.find_all('tr')
    banks_exchange_rate_dictionary = []
    

    for row in rows:
        bank_detail_list = []
        #print("\n"+ str(row.text))
        cells = row.find_all("td")
        for cell in cells:
   
            bank_row = row

            cell_values = []
            for cell in bank_row:
                cell_values.append(cell.text)

        bank = cell_values[2]
        buy_price = cell_values[3]
        sell_price = cell_values[4]


        bank_detail_list.append(bank.strip())
        bank_detail_list.append(buy_price.strip())
        bank_detail_list.append(sell_price.strip())


        banks_exchange_rate_dictionary.append(bank_detail_list)

        #print(banks_exchange_rate_dictionary)
    banks_exchange_rate_dictionary.pop(0)
    return banks_exchange_rate_dictionary

        



