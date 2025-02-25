from django.shortcuts import redirect, render
from .models import Messages
from .forms import MessagesForm
#from accounts.models import Main_user
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings



@login_required
def chat_page(request):
    
    error = ''
    if request.method == "POST":
        if request.user.is_authenticated:        
            
            #получаем список последних сообщений пользователя и сейчашнее время
            current_user_messages = Messages.objects.filter(name=request.user.username).order_by('-created_at')
            now = timezone.now()

            #проверяем, что либо у пользователя не было сообщнений либо его ппоследнее сообщение было отправленно досточно поздно
            if not current_user_messages or (now - current_user_messages[0].created_at).total_seconds() > settings.MESSAGE_SEND_COOLDOWN:
                form = MessagesForm(request.POST, user=request.user)
                if form.is_valid():
                    form.save()
                else:
                    error = 'форма неверна'
            else:
                error = f'Вы можете отправить сообщение через {settings.MESSAGE_SEND_COOLDOWN - (now - current_user_messages[0].created_at).total_seconds()} секунд'
            
        else:
            return redirect('login')      
        
    form = MessagesForm(user=request.user)
    
    messages = Messages.objects.order_by('-created_at')  
    data = {
        'messages':messages,
        'form': form,
        'error': error
    }


    return render(request, 'main/chat_page.html', data) 



class MessageDetailView(DetailView):
    model = Messages
    template_name = 'main/details_view.html'
    context_object_name = 'message'

class MessageUpdateView(UpdateView):
    model = Messages
    template_name = 'main/update_view.html'
    fields = ['name', 'message']


