from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, RequirementsViewSet, MessagesViewSet, JournalsViewSet, PapersViewSet, CategoriesViewSet, AuthorViewSet

router = DefaultRouter()
router.register('faq', FAQViewSet)
router.register('requirements', RequirementsViewSet)
router.register('messages', MessagesViewSet)
router.register('journals', JournalsViewSet)
router.register('papers', PapersViewSet)
router.register('categories', CategoriesViewSet)
router.register('author', AuthorViewSet)

urlpatterns = [
    
]
urlpatterns+=router.urls