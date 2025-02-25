from django.urls import path
from .views import CustomLoginView, register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('reg/', register, name='reg'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
