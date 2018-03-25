from rest_framework import serializers
from . models import sensors
class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=sensors
        fields='__all__'
