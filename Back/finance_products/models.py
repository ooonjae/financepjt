from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) #금융 상품 코드
    kor_co_nm = models.TextField() #금융 회사 명
    fin_prdt_nm = models.TextField() #금융 상품 명
    etc_note = models.TextField() #금융 상품 설명
    join_deny = models.IntegerField() #가입제한 (1: 제한 없음 2: 서민전용 3: 일부제한)
    join_member = models.TextField() #가입 대상
    join_way = models.TextField() #가입 방법
    spcl_cnd = models.TextField() #우대 조건
 
class DepositProps(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    minimum_input = models.IntegerField()
    maximum_input = models.IntegerField()
    for_middle_class = models.IntegerField()
    for_first_user = models.FloatField()
    for_salary_man = models.FloatField()
    for_elder = models.FloatField()
    for_young = models.FloatField()
    pass


class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) #금융 상품 코드
    kor_co_nm = models.TextField() #금융 회사 명
    fin_prdt_nm = models.TextField() #금융 상품 명
    etc_note = models.TextField() #금융 상품 설명
    join_deny = models.IntegerField() #가입제한 (1: 제한 없음 2: 서민전용 3: 일부제한)
    join_member = models.TextField() #가입 대상
    join_way = models.TextField() #가입 방법
    spcl_cnd = models.TextField() #우대 조건
    pass



class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField() #금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length= 100) # 저축 금리 유형명
    intr_rate = models.FloatField() #저축 금리
    intr_rate2 = models.FloatField() #최고 우대 금리
    save_trm = models.IntegerField() #저축기간 (단위 : 개월 )
    pass


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField() #금융 상품 코드
    rsrv_type = models.TextField()
    intr_rate_type_nm = models.CharField(max_length= 100) # 저축 금리 유형명
    intr_rate = models.FloatField() #저축 금리
    intr_rate2 = models.FloatField() #최고 우대 금리
    save_trm = models.IntegerField() #저축기간 (단위 : 개월 )
    pass


