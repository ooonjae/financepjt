from django.shortcuts import render
from django.contrib.auth import get_user
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from .serializers import CustomRegisterSerializer,Customuser
from rest_framework.decorators import api_view
from finance_products.models import DepositProducts, DepositOptions, SavingProducts, DepositProps
from finance_products.serializers import DepositProductsSerializers, DepositOptionsSerializers, DepositPropsSerializers

# Create your views here.

@api_view(['GET','PUT'])
def profile(request):
    if request.method == 'GET':
        user = CustomRegisterSerializer(request.user)
        print(user.data.get('financial_products'))
        products_list = user.data.get('financial_products').split(',')
        return_lst = list(map(lambda x: DepositProductsSerializers(DepositProducts.objects.get(fin_prdt_cd = x)).data, products_list))
        print(len(return_lst))
        context = {
            'user' : user.data,
            'pk' : request.user.pk,
            'products' : return_lst
        }
        return JsonResponse(context)
    
    elif request.method == 'PUT':
        user = get_object_or_404(User, pk=request.user.id)
        print(user)
        serializer = Customuser(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




@api_view(['GET',])
def getRecommendation(request):
    user = Customuser(request.user).data
    products_already_has = user['financial_products'].split(',')
    print(products_already_has)
    candidates = DepositOptions.objects.all()
    serializers = DepositOptionsSerializers(candidates, many = True).data
    print('==============================================================')
    print(serializers[0])
    print(serializers[0].get('product')['fin_prdt_cd'])
    print('==============================================================')

    new_list = [[i, serializers[i].get('intr_rate')] for i in range(len(candidates))]
    new_list_property = [[] for i in range(len(candidates))]
    print(new_list)
    bank_already_has = list(map(lambda x: DepositProductsSerializers(DepositProducts.objects.get(fin_prdt_cd = x)).data.get('kor_co_nm'), products_already_has))
    user['salary']
    print(bank_already_has)
    # 주거래은행 찾기
    
    dic = {}
    if bank_already_has:
        for bank in bank_already_has:
            dic[bank_already_has.count(bank)] = dic.get(bank_already_has.count(bank), set()) | {bank}
    print(dic)
    max_bank_num = max(dic.keys())



    def check_grade(i):
        # 주거래 은행 보내줌
        # 각자요소들에 적용될 것

        # 이미 있는 상품이면 추천하지 않는다
        if serializers[i].get('product')['fin_prdt_cd'] in products_already_has:
            return -float('inf')
        
        res = new_list[i][1]
        # 그러나 주거래 은행이면 가점을 준다.
        if serializers[i].get('product')['kor_co_nm'] in dic[max_bank_num]:
            print(i,'번째 주거래 은행 가점 적용 ')
            new_list_property[i].append(1)
            res += 0.5

        if not new_list[i][1]:
            return -float('inf')
        # 추천한 상품의 특성을 가져온다
        props = DepositPropsSerializers(DepositProps.objects.get(product = DepositProducts.objects.get(fin_prdt_cd = serializers[i].get('fin_prdt_cd')))).data
        if i == 22:
            print(props, 'props예시')
        if user['money'] > 1000000000 & props['for_middle_class'] == 2:
            return -float('inf')
        # 예금의 경우 -> 지금 가지고 있는 돈이 이것보다 적으면 추천하지 않는다.
        if props['minimum_input'] > user['money'] * 0.7:
            return -float('inf')
        
        # 이 은행과 관련된 상품이 없으면서 은행에서 첫 사은품용 금리가 있다면 추가한다.
        if props['for_first_user'] and serializers[i].get('product')['kor_co_nm'] not in bank_already_has:
            print('첫은행 효과', i, '번째 적용')
            new_list_property[i].append(2)

            # print(type(props['for_first_user']))
            res += props['for_first_user'] * 1.5
        if user['age'] > 65 and props['for_elder']:
            print('노인 효과', i, '번째 적용')
            new_list_property[i].append(3)

            res += props['for_first_user']
        elif 19 <= user['age'] <= 34 and props['for_young']:
            new_list_property[i].append(4)
            print('MZ 효과', i, '번째 적용')
            res += props['for_first_user']

        if user['salary'] >= 1000000 and props['for_salary_man']:
            new_list_property[i].append(5)
            print('급여 이체', i, '번째 적용')
            res += props['for_salary_man']

        return res
    # 실행 파트
    for i in range(len(candidates)):
        new_list[i][1] = check_grade(i)

    new_list.sort(key = lambda x : x[1], reverse=True)
    print(new_list)
    print(new_list_property)
    
    start = 0
    return_serializer = []
    while start < 3:
        return_serializer.append({
            'product' : serializers[new_list[start][0]],
            'properties' : new_list_property[new_list[start][0]],
            'total' : round(new_list[start][1], 2)
        })
        start += 1

    return Response(return_serializer)


