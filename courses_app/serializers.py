from rest_framework.validators import UniqueTogetherValidator

from courses_app.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']


        # Такое можно сделать если инфа приходит с фронта и поддерживает пост
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.objects.all(),
        #         fields=['name', 'duration', 'price']
        #     )
        # ]

