from django.contrib import admin
from .models import FAQ, Requirements, Messages, Journals, Papers, Categories, Author

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)

@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_viewed')
    search_fields = ('name', 'email', 'message')
    list_filter = ('is_viewed', 'created_at')

@admin.register(Journals)
class JournalsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'download_link')
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'created_at')

@admin.register(Papers)
class PapersAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views_count', 'download_link')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'is_reviewer', 'is_staff', 'is_superuser')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    list_filter = ('is_reviewer', 'is_staff', 'is_superuser')
