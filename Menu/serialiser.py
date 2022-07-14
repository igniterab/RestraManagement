from rest_framework import serializers
from .models import FoodCategory, MenuItem, Ingridients, Orders
from staff.serialiser import StaffUserSerializer


class FoodCategorySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return FoodCategory.objects.create(**validated_data)

    class Meta:
        model = FoodCategory
        fields = ('name',)


class MenuItemSerializer(serializers.ModelSerializer):
    foods = FoodCategorySerializer(many=True, read_only=True)

    def create(self, validated_data):
        return MenuItem.objects.create(**validated_data)

    class Meta:
        model = MenuItem
        fields = ('foods', 'name', 'category', 'description', 'available', 'price', 'is_veg', 'quantity','reciepe')


class IngridientsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Ingridients.objects.create(**validated_data)

    class Meta:
        model = Ingridients
        fields = ('name', 'description', 'available', 'quantity')


class OrdersSerializer(serializers.ModelSerializer):
    staffuser = StaffUserSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

    class Meta:
        model = Orders
        fields = ('staffuser', 'customer_name', 'mobile', 'table_num', 'is_accepted', 'total', 'payment_method', 'delievery_boy','prep_time', )
