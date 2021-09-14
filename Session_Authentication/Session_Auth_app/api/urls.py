
from django.urls import path,include
from Session_Auth_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('emps', views.EmpModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
]