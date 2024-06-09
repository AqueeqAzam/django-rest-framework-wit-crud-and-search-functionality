from django.shortcuts import render
from rest_framework import generics, filters
from .models import Student
from .serializer import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentSearch(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'age']
    print('first_name')
    print('age')
    
