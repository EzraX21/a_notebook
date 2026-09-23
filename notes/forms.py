# notes/forms.py
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'tag', 'is_mastered']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输入标题或知识点名称'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '输入详细内容、错题解析...'}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例如：MySQL、Python循环...'}),
            'is_mastered': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': '标题',
            'content': '详细内容',
            'tag': '标签',
            'is_mastered': '已掌握',
        }