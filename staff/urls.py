from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/staff_user/$', views.StaffUserView.as_view()),
    
]
