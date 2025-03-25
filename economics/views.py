from django.shortcuts import render
from django.utils import timezone
import xml.etree.ElementTree as ET
from xml.dom import minidom
import requests
from datetime import datetime, timedelta
from utils import openai_requests
from .models import ExchangeRateSummary

# Create your views here.
def indicators(request):
    args = ""
    historical_exchange_rate_sell = get_historical_exchange_rate_sell()
    historical_exchange_rate_buy = get_historical_exchange_rate_buy()
    usd_reserves = get_usd_reserves()
    
    # Analyze with AI to create summary
    # Get the current date
    current_date = timezone.now().date()

    # Query the ExchangeRateSummary model by the current date
    exchange_rate_summary = ExchangeRateSummary.objects.filter(date=current_date).first()

    # If no summary exists for the current date, create a new one
    if not exchange_rate_summary:
        exchange_rate_summary_text = openai_requests.check_exchange_rate(historical_exchange_rate_buy)
        exchange_rate_summary = ExchangeRateSummary.objects.create(summary=exchange_rate_summary_text)
    else:
        exchange_rate_summary_text = exchange_rate_summary.summary

    #reverse all values
    historical_exchange_rate_buy.reverse()
    historical_exchange_rate_sell.reverse()
    usd_reserves.reverse()

    args = {
        'historical_exchange_rate_sell': historical_exchange_rate_sell,
        'historical_exchange_rate_buy': historical_exchange_rate_buy,
        'usd_reserves': usd_reserves,
        'exchange_rate_summary': exchange_rate_summary_text
    }
    return render(request, "economics/indicators.html", args)

def get_dates(delta):
    # Get the current date
    current_date = datetime.now()

    # Subtract 5 days from the current date
    five_days_ago = current_date - timedelta(days=delta)

    # Format the dates as DD/MM/YYYY
    current_date_formatted = current_date.strftime('%d/%m/%Y')
    five_days_ago_formatted = five_days_ago.strftime('%d/%m/%Y')

    return current_date_formatted, five_days_ago_formatted

# Call the method and store the returned dates in variables

def get_historical_exchange_rate_sell():
    url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos"

    current_date, five_days_ago = get_dates(30)

    payload = {
        "Indicador": "318",
        "FechaInicio": five_days_ago,
        "FechaFinal": current_date,
        "Nombre": "Franz Winiker",
        "SubNiveles": "n",
        "CorreoElectronico": "franznica@gmail.com",
        "token": "F6N2FA11LR" 
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.text)
    else:
        print("Error occurred. Status code:", response.status_code)
        
    # Parse the XML
    dom = minidom.parseString(response.text)

    # Find all INGC011_CAT_INDICADORECONOMIC elements
    data_elements = dom.getElementsByTagName('INGC011_CAT_INDICADORECONOMIC')

    # Iterate over each element and extract data
    historical_exchange_rate_list = []

    for element in data_elements:
        date_and_rate_list = []
        cod_indicador = element.getElementsByTagName('COD_INDICADORINTERNO')[0].firstChild.nodeValue
        fecha = element.getElementsByTagName('DES_FECHA')[0].firstChild.nodeValue
        valor = element.getElementsByTagName('NUM_VALOR')[0].firstChild.nodeValue
        #print("DES_FECHA:", fecha)
        #print("NUM_VALOR:", valor)
        valor = valor.replace("000000","")
        
        # Parse the string into a datetime object
        fecha = datetime.fromisoformat(fecha[:-6])
        fecha = fecha.strftime("%d-%m-%Y")

        date_and_rate_list.append(str(fecha))
        date_and_rate_list.append(valor)
        historical_exchange_rate_list.append(date_and_rate_list)
    return historical_exchange_rate_list

def get_historical_exchange_rate_buy():
    url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos"

    current_date, five_days_ago = get_dates(30)

    payload = {
        "Indicador": "317",
        "FechaInicio": five_days_ago,
        "FechaFinal": current_date,
        "Nombre": "Franz Winiker",
        "SubNiveles": "n",
        "CorreoElectronico": "franznica@gmail.com",
        "token": "F6N2FA11LR" 
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.text)
    else:
        print("Error occurred. Status code:", response.status_code)
        
    # Parse the XML
    dom = minidom.parseString(response.text)

    # Find all INGC011_CAT_INDICADORECONOMIC elements
    data_elements = dom.getElementsByTagName('INGC011_CAT_INDICADORECONOMIC')

    # Iterate over each element and extract data
    historical_exchange_rate_list = []

    for element in data_elements:
        date_and_rate_list = []
        cod_indicador = element.getElementsByTagName('COD_INDICADORINTERNO')[0].firstChild.nodeValue
        fecha = element.getElementsByTagName('DES_FECHA')[0].firstChild.nodeValue
        valor = element.getElementsByTagName('NUM_VALOR')[0].firstChild.nodeValue
        #print("DES_FECHA:", fecha)
        #print("NUM_VALOR:", valor)
        valor = valor.replace("000000","")
        
        # Parse the string into a datetime object
        fecha = datetime.fromisoformat(fecha[:-6])
        fecha = fecha.strftime("%d-%m-%Y")

        #date_and_rate_list.append(str(fecha))
        date_and_rate_list.append(valor)
        historical_exchange_rate_list.append(date_and_rate_list)

    return historical_exchange_rate_list

def get_usd_reserves():
    url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos"

    current_date, five_days_ago = get_dates(10)

    payload = {
        "Indicador": "5970",
        "FechaInicio": five_days_ago,
        "FechaFinal": current_date,
        "Nombre": "Franz Winiker",
        "SubNiveles": "n",
        "CorreoElectronico": "franznica@gmail.com",
        "token": "F6N2FA11LR" 
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Request successful!")
        #print(response.text)
    else:
        print("Error occurred. Status code:", response.status_code)
        
    # Parse the XML
    dom = minidom.parseString(response.text)

    # Find all INGC011_CAT_INDICADORECONOMIC elements
    data_elements = dom.getElementsByTagName('INGC011_CAT_INDICADORECONOMIC')

    # Iterate over each element and extract data
    historical_exchange_rate_list = []

    for element in data_elements:
        try:
            date_and_rate_list = []
            cod_indicador = element.getElementsByTagName('COD_INDICADORINTERNO')[0].firstChild.nodeValue
            fecha = element.getElementsByTagName('DES_FECHA')[0].firstChild.nodeValue
            valor = element.getElementsByTagName('NUM_VALOR')[0].firstChild.nodeValue
            #print("DES_FECHA:", fecha)
            #print("NUM_VALOR:", valor)
            #valor = valor.replace("000000","")
            
            # Parse the string into a datetime object
            fecha = datetime.fromisoformat(fecha[:-6])
            fecha = fecha.strftime("%d-%m-%Y")

            date_and_rate_list.append(str(fecha))
            date_and_rate_list.append("$"+valor)
            historical_exchange_rate_list.append(date_and_rate_list)
        except:
            pass

    return historical_exchange_rate_list