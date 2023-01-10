from django.contrib import admin

# Register your models here.
from .models import *


class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao', 'data_modificacao']
    search_fields = ['nome']


admin.site.register(Pessoa, PessoaAdmin)
