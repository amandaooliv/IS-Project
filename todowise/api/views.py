from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response

from app.models import Course, Subject
from .serializers import CourseSerializer, CourseDetailSerializer

class CourseList(APIView):
    """List all courses."""

    def get(self, request):
        courses = Course.objects.filter(user = request.user)
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetailToDos(APIView):
    """Details a Course."""

    def get(self, request, course_id):
        course = get_object_or_404(Course, pk = course_id, user = request.user)
        serializer = CourseDetailSerializer(course, many = False)
        return Response(serializer.data)

    def delete(self, request, course_id):
        course = get_object_or_404(Course, pk = course_id, user = request.user)
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def put(self, request, course_id):
        course = get_object_or_404(Course, pk = course_id, user = request.user)
        serializer = Course
        DetailSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)