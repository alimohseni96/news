from django.urls import path
from task import views

urlpatterns = [
    path('news/', views.HelloNews.as_view(), name='news'),
]