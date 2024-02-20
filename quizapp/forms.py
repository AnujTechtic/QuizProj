from django.forms import ModelForm
from .models import Students, Departments, Questions, Quizs

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'
    
class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class QuizForm(ModelForm):
    class Meta:
        model = Quizs
        fields = '__all__'