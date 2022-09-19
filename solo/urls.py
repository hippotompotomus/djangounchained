from . import views
from django.urls import path
app_name='solo'
urlpatterns = [
path('', views.MainView.as_view(), name='main'),
]