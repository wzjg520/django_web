from django.contrib import admin

# Register your models here.

from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    # fk_name = 'question_id'

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('内容',               {'fields': ['content'], 'classes': ['hello']}),
        ('日期', {'fields': ['addtime']}),
    ]
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    pass



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)