from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('news' , views.news, name='news'),
]
