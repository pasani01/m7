from rest_framework import viewsets
from .models import FAQ, Requirements, Messages, Journals, Papers, Categories, Author
from .serializers import (
        FAQSerializer, 
        RequirementsSerializer, 
        MessagesSerializer, 
        JournalsSerializer, 
        PapersSerializer, 
        CategoriesSerializer, 
        AuthorSerializer
    )
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['question']
    search_fields = ['question',]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    permission_classes = [IsAuthenticated]

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    ilter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name',]


    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


class JournalsViewSet(viewsets.ModelViewSet):
    queryset = Journals.objects.all()
    serializer_class = JournalsSerializer
    ilter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title','created_at',]
    search_fields = ['title',]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


    def get_queryset(self):
        return Journals.objects.filter(category__name=self.request.query_params.get('category', None))

class PapersViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = PapersSerializer
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


    def get_queryset(self):
        return Papers.objects.filter(author=self.request.user)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]


    def get_queryset(self):
        return Author.objects.filter(user=self.request.user)