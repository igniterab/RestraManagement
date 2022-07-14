from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('Menu.urls')),
    path('staff/', include('staff.urls')),
]
