from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chat_page, name="main_chat"),
    path('<int:pk>', views.MessageDetailView.as_view(), name="message_detail"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


