from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    year = models.PositiveIntegerField()
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.school.abbreviation} - Year {self.year}/{self.section}"

    class Meta:
        ordering = ['year', 'section']


class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
