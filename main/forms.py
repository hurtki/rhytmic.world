from .models import Messages
from django.forms import ModelForm, TextInput

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'message']

        widgets = {
            'name': TextInput(attrs={
                'placeholder':"Ваше имя"
            }),
            'message': TextInput(attrs={
                'placeholder':"сообщение"
            })
        }