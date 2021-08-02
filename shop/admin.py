from django.contrib import admin
from . models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catadmin)


class Prodadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','img']
    list_editable = ['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,Prodadmin)
