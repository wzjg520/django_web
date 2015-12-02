from django.contrib import admin

# Register your models here.

from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('内容',               {'fields': ['content'], 'classes': ['hello']}),
        ('日期', {'fields': ['addtime']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['content', 'addtime', 'was_published_recently']
    list_filter = ['addtime', 'content']
    list_per_page = 15
    search_fields = ['content', 'addtime']

class ChoiceAdmin(admin.ModelAdmin):
    pass



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)