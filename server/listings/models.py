from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from rest_framework.authtoken.admin import User


class Categories(MPTTModel):
    name = models.CharField(max_length=300, verbose_name="Название")
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True,
                            verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# Create your models here.
class Listings(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='users_listings', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories,
                                 verbose_name='Категория',
                                 related_name='category_listings',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
