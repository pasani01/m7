from rest_framework import serializers
from .models import Article
from django.utils.translation import gettext_lazy as _

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at']