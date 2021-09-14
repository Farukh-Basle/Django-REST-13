from Session_Auth_app.models import Emp
from .serializers import EmpSerializer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import redirect,render

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAdminUser

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EmpModelViewSet(ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


#We have added this directly inside settings.py file so no need
#   define it here

# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (IsAuthenticated,)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAdminUser,)

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)