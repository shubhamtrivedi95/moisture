from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import sensors
from . serializers import employeesSerializer
class sensorList(APIView):
    def get(self,request):
        sensors_details=sensors.objects.all()
        serializer=employeesSerializer(sensors_details,many=True)
        return Response(serializer.data)