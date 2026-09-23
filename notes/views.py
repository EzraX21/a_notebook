# notes/views.py
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm

def question_list(request):
    """显示错题列表"""
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'notes/question_list.html', context)

def add_question(request):
    """添加错题的视图"""
    if request.method == 'POST':
        # 如果是 POST 请求，说明用户提交了表单
        form = QuestionForm(request.POST)
        if form.is_valid():
            # 表单验证通过，保存到数据库
            form.save()
            return redirect('question_list')  # 保存后跳转到列表页
    else:
        # 如果是 GET 请求，显示空表单
        form = QuestionForm()
    
    return render(request, 'notes/add_question.html', {'form': form})