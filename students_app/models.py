from django.db import models
from courses_app.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [(FEMALE, 'female'),
                      (MALE, 'male')
                      ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['first_name']
        unique_together = (
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',
            'email',
            'gender',
            'course'
        )

# Это валидация заглавных букв
#     def save(self, *args, **kwargs):
#         for field_name in ['first_name', 'last_name']:
#             val = getattr(self, field_name, False)
#             if val:
#                 setattr(self, field_name, val.capitalize())
#         super(Student, self).save(*args, **kwargs)
# 2 метод
    # def saves(self, *args, **kwargs):
    #     self.first_name = self.first_name.capitalize()
    #     self.last_name = self.last_name.capitalize()
