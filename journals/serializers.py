from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import FAQ, Requirements, Messages, Journals, Papers, Categories, Author
from django.contrib.auth.models import User


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class RequirementsSerializer(ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'


class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        extra_kwargs = {
            'is_viewed': {'read_only': True},
        }


class JournalsSerializer(ModelSerializer):
    title = SerializerMethodField('get_title')
    article = SerializerMethodField('get_article')

    class Meta:
        model = Journals
        fields = (
            "title", 'article', 'title_uz', 'title_ru', 'article_uz', 'article_ru',
            'references', 'created_at', 'download_link', 'category',
        )
        extra_kwargs = {
            'title_uz': {'write_only': True},
            'title_ru': {'write_only': True},
            'article_uz': {'write_only': True},
            'article_ru': {'write_only': True},
        }

    def get_title(self, obj):
        if self.context.get('lang') == 'ru':
            return obj.title_ru
        return obj.title_uz

    def get_article(self, obj):
        if self.context.get('lang') == 'ru':
            return obj.article_ru
        return obj.article_uz

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang', 'uz')
        context['lang'] = lang
        return context


class PapersSerializer(ModelSerializer):
    title = SerializerMethodField('get_title')
    article = SerializerMethodField('get_article')

    class Meta:
        model = Papers
        fields = (
            "title", 'article', 'title_uz', 'title_ru', 'article_uz', 'article_ru',
            'author', 'views_count', 'created_at', 'download_link',
        )
        extra_kwargs = {
            'views_count': {'read_only': True},
            'created_at': {'read_only': True},
            'title_uz': {'write_only': True},
            'title_ru': {'write_only': True},
            'article_uz': {'write_only': True},
            'article_ru': {'write_only': True},
        }

    def get_title(self, obj):
        if self.context.get('lang') == 'ru':
            return obj.title_ru
        return obj.title_uz

    def get_article(self, obj):
        if self.context.get('lang') == 'ru':
            return obj.article_ru
        return obj.article_uz

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang', 'uz')
        context['lang'] = lang
        return context


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }
