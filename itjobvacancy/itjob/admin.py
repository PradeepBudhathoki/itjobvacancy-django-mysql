from django.contrib import admin
from .models import Vacancy,Company,Skill,Category


admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Vacancy)
