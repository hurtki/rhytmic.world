from django.db import models

class Messages(models.Model):
    name = models.CharField('Имя отправителя', max_length=20)
    message = models.CharField('Текст сообщения', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def get_absolute_url(self):
        return f'/{self.id}'

    

    def __str__(self):
        return self.name

