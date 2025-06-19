from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150)
    chat_id = models.CharField(max_length=100)

    def __str__(self):
        return self.username
