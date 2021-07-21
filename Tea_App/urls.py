from django.conf.urls import url
from django.urls import path
from Tea_App import views


app_name='Tea_App'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog-details/<int:pk>/', views.blog_details, name="blog_details"),
    path('blog/', views.blog, name="blog"),
    path('help/', views.help, name="help"),
    path('tea_details/', views.tea_details, name="tea_details"),
    path('types/', views.types, name="types")
]