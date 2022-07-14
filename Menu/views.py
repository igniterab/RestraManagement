from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from staff.models import StaffUser
from .models import FoodCategory, MenuItem, Orders, Ingridients
from .serialiser import FoodCategorySerializer, MenuItemSerializer, OrdersSerializer, IngridientsSerializer
from django.http import Http404



class FoodCategoryView(APIView):
    """
    List all FoodCategory, or create a new FoodCategory.
    """
    query = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(self.query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs): 
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


class MenuItemView(APIView):
    """
    List all MenuItem, or create a new MenuItem.
    """
    query = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(self.query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


class OrdersView(APIView):
    """
    List all Orders, or create a new Orders.
    """
    query = Orders.objects.all()
    serializer_class = OrdersSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(self.query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


class IngridientsView(APIView):
    """
    List all Ingridients, or create a new Ingridients.
    """
    query = Ingridients.objects.all()
    serializer_class = IngridientsSerializer
    
    def get(self, request, format=None):
        serializer = self.serializer_class(self.query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)