import requests
from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import DepositProductsSerializers, DepositOptionsSerializers , SavingProductsSerializers, SavingOptionsSerializers, DepositPropsSerializers
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, DepositProps
from pprint import pprint
import json
# Create your views here.

BASE_URL = "https://finlife.fss.or.kr/finlifeapi/"

def voirMoore(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0
    while i <= N-M:
        j = M - 1

        while j >= 0:
            if pattern[j] != text[i+j]:
                move = find(pattern, text[i + M - 1])   
                break
            j = j - 1
        if j == -1:
            return i
        else:
            i += move
    return False

def find(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern) -i -1
    return len(pattern)



@api_view(['GET'])
def getDepositProduct(request): 
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.PRODUCT_API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
        }
    response = requests.get(URL, params=params).json()
    for item in response.get('result').get('baseList'):

        # 상품 특성 분석


        REFINE_COND = [item['spcl_cnd'].replace(' ', '').replace('\t', '').replace('\n', ''), item['etc_note'].replace(' ', '').replace('\t', '').replace('\n', '')]
        PATTERNS_FORMONEY = ['만원']
        PATTERNS_FORINIT = ['첫', '처음', '신규가입', '신규고객']
        PATTERNS_FORSALARYMAN = ['급여']
        PATTERNS_FORELDER = ['65세', '노인', '고령자', '60세', '61세', '62세', '70세']
        PATTERNS_YOUNG = ['19세', '20세', '34세', '25세', '청년', '청소년']

        # 최소 금액 
        depositprops = {
            'minimum_input' : 0,
            'maximum_input' : 0,
            'for_middle_class' : 0,
            'for_first_user' : 0,
            'for_salary_man' : 0,
            'for_elder' : 0,
            'for_young' : 0,
        }
        for pattern in PATTERNS_FORMONEY:
            idx = voirMoore(pattern, REFINE_COND[1])
            idx -= 1
            stack = []
            if idx:
                while REFINE_COND[1][idx].isdigit() or REFINE_COND[1][idx] in ['백', '십', '천']:
                    stack.append(REFINE_COND[1][idx])
                    idx -= 1
            if stack:
                start = 0
                while stack:
                    next = stack.pop()
                    if next.isdigit():
                        start *= 10
                        start += int(next)
                    else:
                        if next == '백':
                            start *= 100
                        elif next == '천':
                            start *= 1000
                        else:
                            start *= 10
                # print(start * 10000)
                depositprops['minimum_input'] = start * 10000

        # print('---------------------------- 이번에는 첫고객확인')
        
        # print(REFINE_COND[0].split('%'))
        candidates = REFINE_COND[0].split('%')
        for candidate in candidates:
            patterns = PATTERNS_FORINIT
            for pattern in patterns:
                if voirMoore(pattern, candidate):
                    idx = len(candidate) - 1
                    while candidate[idx].isdigit() or candidate[idx] == '.':
                        idx -= 1
                    if idx != len(candidate) - 1:
                        # print(float(candidate[idx + 1:]), candidate)
                        depositprops['for_first_user'] = float(candidate[idx + 1:])
                    break
            patterns = PATTERNS_FORSALARYMAN
            for pattern in patterns:
                if voirMoore(pattern, candidate):
                    idx = len(candidate) - 1
                    while candidate[idx].isdigit() or candidate[idx] == '.':
                        idx -= 1
                    if idx != len(candidate) - 1:
                        # print(float(candidate[idx + 1:]), candidate)
                        depositprops['for_salary_man'] = float(candidate[idx + 1:])
                    break

            patterns = PATTERNS_FORELDER
            for pattern in patterns:
                if voirMoore(pattern, candidate):
                    idx = len(candidate) - 1
                    while candidate[idx].isdigit() or candidate[idx] == '.':
                        idx -= 1
                    if idx != len(candidate) - 1:
                        # print(float(candidate[idx + 1:]), candidate)
                        depositprops['for_elder'] = float(candidate[idx + 1:])
                    break
            

            patterns = PATTERNS_YOUNG
            for pattern in patterns:
                if voirMoore(pattern, candidate):
                    idx = len(candidate) - 1
                    while candidate[idx].isdigit() or candidate[idx] == '.':
                        idx -= 1
                    if idx != len(candidate) - 1:
                        # print(float(candidate[idx + 1:]), candidate)
                        depositprops['for_young'] = float(candidate[idx + 1:])
                    break
        print(depositprops)
        try:
            Existedmodel = DepositProducts.objects.get(cur_nm = item.get('cur_nm'))
            serializer = DepositProductsSerializers(instance = Existedmodel, data = item)
        except:
            serializer = DepositProductsSerializers(data = item)
        if serializer.is_valid():
            serializer.save()
        fin_prdt_cd = item.get('fin_prdt_cd')
        product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)

        if item.get('max_limit'):
            depositprops['maximum_input'] = item.get('max_limit')
        if item.get('join_deny'):
            depositprops['for_middle_class'] = item.get('join_deny')
        try:
            Existedmodel = DepositProps.objects.get(product = product)
            serializer = DepositPropsSerializers()(instance = Existedmodel, data = depositprops)
        except:
            serializer = DepositPropsSerializers(data = depositprops)
        if serializer.is_valid(raise_exception=True):
            # print('됐음')
            serializer.save(product = product)


    for item in response.get('result').get('optionList'):
        fin_prdt_cd = item.get('fin_prdt_cd')
        if not item['intr_rate']:
            item['intr_rate'] = -1
        product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
        try:
            Existedmodel = DepositOptions.objects.get(cur_nm = item.get('cur_nm'))
            serializer = DepositOptionsSerializers(instance = Existedmodel, data = item)
        except:
            serializer = DepositOptionsSerializers(data = item)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
    return JsonResponse({ 'response' : response })



@api_view(['GET'])
def getSavingProduct(request):
    URL = BASE_URL + 'savingProductsSearch.json?'
    params = {
        'auth': settings.PRODUCT_API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
        }
    response = requests.get(URL, params=params).json()
    for item in response.get('result').get('baseList'):
        # print(item)
        try:
            Existedmodel = SavingProducts.objects.get(cur_nm = item.get('cur_nm'))
            serializer = SavingProductsSerializers(instance = Existedmodel, data = item)
        except:
            serializer = SavingProductsSerializers(data = item)
        if serializer.is_valid():
            serializer.save()

    for item in response.get('result').get('optionList'):
        fin_prdt_cd = item.get('fin_prdt_cd')
        if not item['intr_rate']:
            item['intr_rate'] = -1
        product = SavingProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
        try:
            Existedmodel = SavingOptions.objects.get(cur_nm = item.get('cur_nm'))
            serializer = SavingOptionsSerializers(instance = Existedmodel, data = item)
        except:
            serializer = SavingOptionsSerializers(data = item)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
            print(serializer)

    return JsonResponse({ 'response' : response })

    pass
@api_view(['GET'])
def clientDepositProduct(request):
    objects = DepositProducts.objects.all()
    serializer = DepositProductsSerializers(objects, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def clientDepositCompare(request, ptcd1, ptcd2):
    objects1 = DepositProducts.objects.get(fin_prdt_cd = ptcd1)
    objects1_options = DepositOptions.objects.filter(product = objects1)
    objects2 = DepositProducts.objects.get(fin_prdt_cd = ptcd2)
    objects2_options = DepositOptions.objects.filter(product = objects2)
    context = {
     ptcd1 : DepositOptionsSerializers(objects1_options, many = True).data,
     ptcd2 : DepositOptionsSerializers(objects2_options, many = True).data
     }
    return Response(context)

@api_view(['GET'])
def clientDepositDetail(request, ptcd1):
    objects1 = DepositProducts.objects.get(fin_prdt_cd = ptcd1)
    objects1_serializer = DepositProductsSerializers(objects1)
    return Response(objects1_serializer.data)

@api_view(['GET'])
def top_rate(request):
    options = DepositOptions.objects.all()

    # for option in options:
    #     print(option.intr_rate2)
    option = max(options, key =lambda x: x.intr_rate2)
    # option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
    serializer_option = DepositOptionsSerializers(option)
    product = option.product
    serializer_product = DepositProductsSerializers(product)
    json = { 
        'deposit-product' : serializer_product.data,
        'option' : serializer_option.data 
     }
    return Response(json)



# @api_view(['GET'])
# def recommend(request):
#     '''
#     1. 리퀘스트 유저 정보를 받아오기 - 머니 , 연봉 , 가입한 상품목록
#     2. if 머니 <= 10억 : is서민 = true  
#     3. 가입한 상품이 있으면 -> 주거래은행 파악 가능 //
#     4. 정기예금 리스트를 순회하면서 
#     '''
#     pass