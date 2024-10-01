from .models import TutorReg,Student
from rest_framework import serializers
class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TutorReg
        fields = ['id','username','password', 'mobileno','fname']

class StduentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields=['rno','name','branch','fee']