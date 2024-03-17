from django.shortcuts import render
from django.conf import settings
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
import json
import requests
# Create your views here.


# 환율을 주기적으로 요청

#일단 url요청이 오면 요청하게 만들기.
@api_view(['GET'])
def getExchangeRate(request):
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
                print(arg)
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
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def clientExchangeRate(request):
    rate = ExchangeRate.objects.all()
    serializer = ExchangeRateSerializer(rate, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

