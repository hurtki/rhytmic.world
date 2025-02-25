from django.shortcuts import render
from .models import Messages
from .forms import MessagesForm
from django.views.generic import DetailView, UpdateView

def chat_page(request):
    form = MessagesForm()
    error = ''
    if request.method == "POST":
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'форма неверна'
    
    
    
    
    messages = Messages.objects.order_by('-created_at')  
    data = {
        'messages':messages,
        'form':form,
        'error': error,
        

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


