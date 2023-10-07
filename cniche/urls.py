"""cniche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from survey.models import Survey
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins

# Serializers define the API representation.
class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        exclude = [ 'url' ]

# ViewSets define the view behavior.
class SurveyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletter.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
