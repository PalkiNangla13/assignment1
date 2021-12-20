from rest_framework import serializers
from rest_framework import ProductItem

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductItem

        fields = '__all__'