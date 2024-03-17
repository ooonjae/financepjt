from celery import shared_task
from time import sleep
from .models import ExchangeRate
from django.conf import settings
from .serializers import ExchangeRateSerializer
import requests

@shared_task
def print_one():
    print(1)
    
import django
django.setup()

    
@shared_task
def refreshData():
    EXCHANGE_RATE_URL = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/"
    EXCHANGE_RATE_API_KEY = settings.EXCHANGE_RATE_API_KEY
    params = {
        'data' :  'AP01',
        'authkey' : EXCHANGE_RATE_API_KEY,
    }
    # serializers = ExchangeRateSerializer(data = requests.get(EXCHANGE_RATE_URL, params = params).json(), many=True)
    response = requests.get(EXCHANGE_RATE_URL, params = params).json()
    # print(response)
    for item in response:
        if item.get('result') == 1:
            for arg in item:
                if type(item[arg]) == str:
                    item[arg] = item[arg].replace(',', '')     
            try:
                Existedmodel = ExchangeRate.objects.get(cur_nm = item.get('cur_nm'))
                serializer = ExchangeRateSerializer(instance = Existedmodel, data = item)
            except:
                serializer = ExchangeRateSerializer(data = item)
            if serializer.is_valid():
                serializer.save()
            else:
                pass
        else:
            pass 