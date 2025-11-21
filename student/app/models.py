from django.db import models

class Students(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    midname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    bday = models.CharField(max_length=10)
    group = models.CharField(max_length=10)

class Exams(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE, primary_key=True)
    grade_first = models.IntegerField()
    grade_second = models.IntegerField()
    grade_third = models.IntegerField()
    grade_fourth = models.IntegerField()
    result = models.FloatField(blank=True, null=True)