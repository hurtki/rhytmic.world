from .models import Messages
from django.forms import ModelForm, TextInput
from django.forms import ModelForm, TextInput, HiddenInput


class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'message']

        widgets = {
            'name': HiddenInput(),
            'message': TextInput(attrs={
                'placeholder':"сообщение"
            })
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем пользователя, если передан
        super().__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.username
