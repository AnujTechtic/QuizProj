from django.db import models
import uuid, datetime
# Create your models here.
class Students(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique= True, editable = False, primary_key = True)
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    quiz = models.ForeignKey("Quizs",on_delete=models.CASCADE,blank=True)
    # DOB = models.DateField()    
    def __str__(self):
        return self.name

class Departments(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique= True, editable = False, primary_key = True)
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    def __str__(self):
        return self.name

class Questions(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique= True, editable = False, primary_key = True)
    question = models.CharField(max_length = 500)
    option_1 = models.CharField(max_length = 500)
    option_2 = models.CharField(max_length = 500)
    option_3 = models.CharField(max_length = 500)
    option_4 = models.CharField(max_length = 500)
    correct_option = models.IntegerField()
    quiz = models.ForeignKey("Quizs",on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.question

class Results(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique= True, editable = False, primary_key = True)
    student_choice = models.IntegerField()
    is_valid = models.BooleanField()
    # marks_scored = models.IntegerField()
    

class Quizs(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique= True, editable = False, primary_key = True)
    dept = models.ForeignKey("Departments",on_delete=models.CASCADE,blank=True)
    date = models.DateField()
    total_questions = models.IntegerField()
    total_marks = models.IntegerField()
    
    
