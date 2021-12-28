"""
Definition of models.
"""

from django.db import models


# Create your models here.
from datetime import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликован")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "Пост"
        verbose_name_plural = "Пост"

class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Пост")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий к посту"
        ordering = ["-date"]

class Orders(models.Model):
    fio = models.CharField(max_length = 1000, verbose_name = 'ФИО')
    email = models.CharField(max_length = 1000, verbose_name = "E-mail")
    phone = models.CharField(max_length = 11, verbose_name = "Телефон")
    date = models.CharField(max_length = 1000, verbose_name = 'Дата', null=True)
    sum = models.IntegerField(verbose_name = 'Сумма', null=True);
    tickets = models.TextField(verbose_name="Билеты", null=True);

    def __str__(self):
        return self.fio + "; На сумму " + str(self.sum);

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

admin.site.register(Blog)
admin.site.register(Orders)
