from rest_framework import serializers
from .models import Car , Expense , Income

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class expenseSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        
class incomeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Income
        fields = '__all__'
        