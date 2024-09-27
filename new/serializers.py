from django.contrib.auth import get_user_model
from rest_framework import serializers

from new.models import Category, News, Comment, Sud, Jurnalistik, Yangilik_sub

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'order']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'created_at']


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'subtitle', 'content', 'category',  'image', 'link', 'time', 'tag', 'comments',
                  'category_id', 'view_count', 'created_at']



class SudSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Sud
        fields = ['id', 'title', 'subtitle', 'content', 'image', 'link', 'time', 'tag', 'comments', 'view_count',
                  'created_at']


class JurnalistikSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Jurnalistik
        fields = ['id', 'title', 'subtitle', 'content', 'image', 'link', 'time', 'tag', 'comments', 'view_count',
                  'created_at']


class Yangilik_subSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Yangilik_sub
        fields = ['id', 'title', 'subtitle', 'content', 'image', 'link', 'time', 'tag', 'comments', 'view_count',
                  'created_at']
