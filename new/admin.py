from django.contrib import admin
from .models import Category, News, Comment, Sud, Jurnalistik, Yangilik_sub
from modeltranslation.admin import TranslationAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'order',)
    search_fields = ('name_uz',)
    fields = ('name_uz', 'name_ru', 'order',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'created_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'category', 'image',
              'link', 'time_uz', 'time_ru',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at',)
    search_fields = ('comment', 'user__username',)
    fields = ('news', 'user', 'comment',)
    readonly_fields = ('created_at',)

@admin.register(Sud)
class SudAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'created_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'image', 'link',
              'time_uz', 'time_ru',)

@admin.register(Jurnalistik)
class JurnalistikAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'created_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'image', 'link',
              'time_uz', 'time_ru',)

@admin.register(Yangilik_sub)
class Yangilik_subAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'created_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'image', 'link',
              'time_uz', 'time_ru',)
