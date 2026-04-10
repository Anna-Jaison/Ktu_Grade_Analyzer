from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Scheme(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Semester(models.Model):
    number = models.IntegerField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

    def __str__(self):
        return f"S{self.number}"


class Subject(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    credits = models.FloatField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    is_elective = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.name}"


# 🔥 UPDATED
class StudentElective(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.subject}"