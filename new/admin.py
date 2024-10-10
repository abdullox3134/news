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
    list_display = ('user_full_name', 'comment', 'created_at',)
    search_fields = ('comment', 'user__full_name',)
    fields = ('news', 'user_full_name', 'comment',)
    readonly_fields = ('created_at', 'user_full_name')

    def user_full_name(self, obj):
        return obj.user.full_name if obj.user and obj.user.full_name else 'User'

    user_full_name.short_description = 'User Full Name'

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
