from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_dispaly = ('__all__',)


admin.site.register(CustomUser, CustomUserAdmin)
