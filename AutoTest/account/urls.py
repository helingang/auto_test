from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.registerView.as_view(), name='register'),
]


