from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Accounts(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return self.user.email
