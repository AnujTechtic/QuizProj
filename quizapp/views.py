from django.shortcuts import render, redirect
from .forms import StudentForm, DepartmentForm, QuestionForm, QuizForm
from . models import Quizs, Questions
# Create your views here.
def home(request):
    return render(request, 'quizapp/Home.html')

def facultyLogin(request):
    form = DepartmentForm()    
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quizCreate')
    context = {'form': form}
    return render(request, 'quizapp/facultyLogin.html', context)

def quizCreate(request):    
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('questionCreate')
    context = {'form': form}
    return render(request, 'quizapp/quiz_details.html', context)

def quizView(request):
    quizs = Quizs.objects.all()
    context ={'quizs': quizs}
    return render(request, 'quizapp/quiz_list.html', context)

def studentRegister(request, pk):
    questions = Questions.objects.filter(id=pk)    
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quizapp/question_list.html/' + questions)
    context = {'form': form, }
    return render(request, 'quizapp/studentregistration.html', context)

def questionView(request, pk):
    quetions = Questions.objects.all()
    quizs = Questions.objects.filter(id=pk)
    context ={'quetions': quetions, 'quizs': quizs}
    return render(request, 'quizapp/question_list.html', context)


def questionCreate(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'quizapp/question_page.html', context)
    