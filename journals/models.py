from django.db import models
from django.contrib.auth.models import User

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Requirements(models.Model):
    title = models.TextField()
    description = models.TextField()

class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

class Journals(models.Model):
    title = models.CharField(max_length=255)
    article = models.TextField()
    references = models.ManyToManyField('Papers')
    papers_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    download_link = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

class Papers(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    article = models.TextField()
    views_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    reference = models.BigIntegerField()
    download_link = models.TextField()
    journal = models.ForeignKey('Journals', on_delete=models.CASCADE)

class Categories(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_reviewer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.BigIntegerField()
    scientific_degree = models.TextField()
    extra_info = models.TextField()
    photo = models.TextField()