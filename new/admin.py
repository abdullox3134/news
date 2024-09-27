from django.contrib import admin
from new.models import Category, News, Comment, Sud, Jurnalistik, Yangilik_sub

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    search_fields = ('name',)
    fields = ('name','order',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tag', 'created_at',)
    search_fields = ('title',)
    fields = ('title', 'subtitle', 'content', 'category', 'image', 'link', 'time', 'tag',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at',)
    search_fields = ('comment', 'user__username',)
    fields = ('news', 'user', 'comment',)
    readonly_fields = ('created_at',)

@admin.register(Sud)
class SudAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'created_at',)
    search_fields = ('title',)
    fields = ('title', 'subtitle', 'content', 'image', 'link', 'time', 'tag',)

@admin.register(Jurnalistik)
class JurnalistikAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'created_at',)
    search_fields = ('title',)
    fields = ('title', 'subtitle', 'content', 'image', 'link', 'time', 'tag',)

@admin.register(Yangilik_sub)
class Yangilik_subAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'created_at',)
    search_fields = ('title',)
    fields = ('title', 'subtitle', 'content', 'image', 'link', 'time', 'tag',)