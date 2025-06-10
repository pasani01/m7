from django.db import models
from django.contrib.auth.models import User


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question[:50]


class Requirements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Categories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or "Kategori yok"


class Papers(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    article_uz = models.TextField()
    article_ru = models.TextField()
    views_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title_uz


class Journals(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    article_uz = models.TextField()
    article_ru = models.TextField()
    references = models.ForeignKey(Papers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_uz


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_reviewer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    scientific_degree = models.TextField()
    extra_info = models.TextField()
    photo = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
