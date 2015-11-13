from django.contrib import admin

# Register your models here.

from .models import *
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('内容',               {'fields': ['content'], 'classes': ['hello']}),
        ('日期', {'fields': ['addtime']}),
    ]

admin.site.register(Question, QuestionAdmin)
