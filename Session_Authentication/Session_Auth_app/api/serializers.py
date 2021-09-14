from rest_framework import serializers
from Session_Auth_app.models import Emp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'