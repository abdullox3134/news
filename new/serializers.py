from django.contrib.auth import get_user_model
from rest_framework import serializers

from new.models import Category, News, Comment, Sud, Jurnalistik, Yangilik_sub

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'order']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    full_name = serializers.SerializerMethodField()  # Use SerializerMethodField to handle null values

    class Meta:
        model = Comment
        fields = ['id', 'user', 'full_name', 'comment', 'created_at']

    def get_full_name(self, obj):
        # Return the user's full_name if available, else return 'Anonymous'
        return obj.user.full_name if obj.user and obj.user.full_name else 'User'



class NewsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'category',
                  'image', 'link', 'time_uz', 'time_ru', 'comments', 'category_id', 'view_count', 'created_at']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None



class SudSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Sud
        fields = ['id', 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'image',
                  'link', 'time_uz', 'time_ru', 'comments', 'view_count', 'created_at']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None


class JurnalistikSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Jurnalistik
        fields = ['id', 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'image',
                  'link', 'time_uz', 'time_ru', 'comments', 'view_count',
                  'created_at']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None


class Yangilik_subSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Yangilik_sub
        fields = ['id', 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'content_uz', 'content_ru', 'image',
                  'link', 'time_uz', 'time_ru', 'comments', 'view_count', 'created_at']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

