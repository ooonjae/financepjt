from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    cur_nm = models.TextField()
    cur_unit = models.TextField()
    deal_bas_r = models.FloatField()
    kftc_bkpr = models.FloatField()
    kftc_deal_bas_r = models.FloatField()
    ten_dd_efee_r = models.IntegerField()
    ttb = models.FloatField()
    tts = models.FloatField()
    yy_efee_r = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=True)
