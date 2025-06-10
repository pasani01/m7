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


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_reviewer', 'is_staff')
    search_fields = ('first_name', 'last_name',)
    list_filter = ('is_reviewer', 'is_staff',)
