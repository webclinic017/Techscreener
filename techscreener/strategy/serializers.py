from rest_framework import serializers
from strategy.models import Strategy

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id',
                  'name',
                  'length',
                  'buy',
                  'sell')