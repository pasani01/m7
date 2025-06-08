from rest_framework import serializers
from .models import (
    FAQ, 
    Requirements, 
    Messages, 
    Journals, 
    Papers, 
    Categories, 
    Author
)
from django.contrib.auth.models import User

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class JournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journals
        fields = '__all__'

class PapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']