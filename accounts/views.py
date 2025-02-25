from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import CustomLoginForm, CustomRegisterForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomLoginForm

    def get(self, request, *args, **kwargs):
        print("Рендерится шаблон: accounts/login.html")  # Проверка в консоли
        return super().get(request, *args, **kwargs)

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним после регистрации
            return redirect("main_chat")  # Перенаправляем на главную
    else:
        form = CustomRegisterForm()

    return render(request, "accounts/registration.html", {"form": form}) 