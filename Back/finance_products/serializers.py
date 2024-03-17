from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts, DepositProps




class DepositOptionsSerializers(serializers.ModelSerializer):
    class DepositProductsSerializers(serializers.ModelSerializer):
        class Meta:
            model = DepositProducts
            fields = '__all__'
    product = DepositProductsSerializers(read_only = True)

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product', )
        

class DepositProductsSerializers(serializers.ModelSerializer):
    depositoptions_set = DepositOptionsSerializers(many = True, read_only = True)
    class Meta:
        model = DepositProducts
        fields = '__all__'
        

class DepositPropsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositProps
        fields = '__all__'
        read_only_fields = ('product', )


class SavingProductsSerializers(serializers.ModelSerializer):
    depositoptions_set = DepositOptionsSerializers(many = True, read_only = True)
    class Meta:
        model = SavingProducts
        fields = '__all__'
 

class SavingOptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product', )

        

        