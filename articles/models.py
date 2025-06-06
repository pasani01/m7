from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name=_("Muallif"))
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    content = models.TextField(verbose_name=_("Kontent"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Tahrirlangan vaqti"))

    def __str__(self):
        return self.title