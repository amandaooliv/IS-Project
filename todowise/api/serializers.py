from rest_framework import serializers
from app.models import Course, Subject

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many = True, read_only = True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'subjects']