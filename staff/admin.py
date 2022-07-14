from django.contrib import admin
from .models import StaffUser

class StaffUserAdmin(admin.ModelAdmin):

    list_display = ('native_name',
    'email',
    'first_name',
    'last_name', 
    'phone_no',
    'busy', )


admin.site.register(StaffUser, StaffUserAdmin)
