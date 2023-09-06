from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Teacher/')
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='Course')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pix = models.ImageField(upload_to='student')
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Event(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title