from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/food_category/$', views.FoodCategoryView.as_view()),
    re_path(r'^api/menu_item/$', views.MenuItemView.as_view()),
    re_path(r'^api/order/$', views.OrdersView.as_view()),
    re_path(r'^api/ingridients/$', views.IngridientsView.as_view()),
]
