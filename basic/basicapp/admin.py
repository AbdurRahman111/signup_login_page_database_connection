from django.contrib import admin
from .models import signup_info
from .models import product_info
# Register your models here.


class dis_sign_info(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'address', 'city', 'vanue']

class dis_prod_info(admin.ModelAdmin):
    list_display = ['name', 'prize', 'discribe']



admin.site.register(signup_info, dis_sign_info)
admin.site.register(product_info, dis_prod_info)