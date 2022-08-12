from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('weather' , views.weather , name='weather'),
]
