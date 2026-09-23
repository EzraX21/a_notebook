from django.contrib import admin
from .models import Question
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'is_mastered', 'created_at')
    list_filter = ('is_mastered', 'tag')
    search_fields = ('title', 'content')