from django.urls import path
from . import views
urlpatterns = [
    path("" , views.index , name='index'),
    
    path('signup' , views.signup , name='signup'),

    path('login' , views.login , name='login'),

    path('logout', views.logout , name='logout'),

    path('shop' , views.shop , name='shop'),

    path('blog' , views.blog , name='blog'),

    path('blog-single' , views.blog_single , name='blog-single'),

    path('contact', views.contact , name='contact'),
]
