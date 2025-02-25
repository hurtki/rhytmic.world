from django.urls import path
from .views import CustomLoginView, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('reg/', register, name='reg'),
]
