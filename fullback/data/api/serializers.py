from rest_framework import serializers
from data.models import Todoentriesmodel

class TododataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoentriesmodel
        fields = '__all__'