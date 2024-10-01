from .models import TutorReg,Student
from rest_framework import viewsets
from tutorapp.serializers import TutorSerializer,StduentSerializer
class TutorViewSet(viewsets.ModelViewSet):
    queryset = TutorReg.objects.all()
    serializer_class = TutorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StduentSerializer