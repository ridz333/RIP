from django.contrib import admin
from .models import Main

@admin.register(Main)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}