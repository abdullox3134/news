from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from .models import News, Category, Sud, Jurnalistik, Yangilik_sub

from rest_framework import filters, status
from rest_framework.response import Response

from .serializers import CategorySerializer, NewsSerializer, CommentSerializer, SudSerializer, JurnalistikSerializer, \
    Yangilik_subSerializer
from django.contrib.auth.models import User, AnonymousUser


User = get_user_model()



class CategoryListView(ListAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by('order')


@api_view(['GET'])
def categorydetail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, context={'request': request})
    return Response(serializer.data)


class NewsListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-created_at')


@api_view(['GET', 'POST'])
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)

    if request.method == 'GET':
        news.view_count += 1
        news.save()
        serializer = NewsSerializer(news, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Foydalanuvchi tizimga kirmagan bo'lsa, AnonymousUser bo'lishi kerak
            if isinstance(request.user, AnonymousUser):
                # Anonim foydalanuvchini yaratish yoki olish
                anonymous_user, created = User.objects.get_or_create(username='anonymous')  # Anonim foydalanuvchini olish yoki yaratish
                serializer.save(user=anonymous_user, news=news)
            else:
                serializer.save(user=request.user, news=news)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def add_comment(request, news_id):
    news = get_object_or_404(News, id=news_id)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(news=news, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SudListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SudSerializer

    def get_queryset(self):
        return Sud.objects.all().order_by('-created_at')



@api_view(['GET', 'POST'])
def sud_detail(request, pk):
    sud = get_object_or_404(Sud, pk=pk)

    if request.method == 'GET':
        sud.view_count += 1
        sud.save()
        serializer = SudSerializer(sud, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Foydalanuvchi tizimga kirmagan bo'lsa, AnonymousUser bo'lishi kerak
            if isinstance(request.user, AnonymousUser):
                # Anonim foydalanuvchini yaratish yoki olish
                anonymous_user, created = User.objects.get_or_create(username='anonymous')  # Anonim foydalanuvchini olish yoki yaratish
                serializer.save(user=anonymous_user, sud=sud)
            else:
                serializer.save(user=request.user, sud=sud)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class JurnalistikListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = JurnalistikSerializer

    def get_queryset(self):
        return Jurnalistik.objects.all().order_by('-created_at')


@api_view(['GET', 'POST'])
def jurnalistik_detail(request, pk):
    jurnalistik = get_object_or_404(Jurnalistik, pk=pk)

    if request.method == 'GET':
        jurnalistik.view_count += 1
        jurnalistik.save()
        serializer = JurnalistikSerializer(jurnalistik, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Foydalanuvchi tizimga kirmagan bo'lsa, AnonymousUser bo'lishi kerak
            if isinstance(request.user, AnonymousUser):
                # Anonim foydalanuvchini yaratish yoki olish
                anonymous_user, created = User.objects.get_or_create(username='anonymous')  # Anonim foydalanuvchini olish yoki yaratish
                serializer.save(user=anonymous_user, jurnalistik=jurnalistik)
            else:
                serializer.save(user=request.user, jurnalistik=jurnalistik)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Yangilik_subListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Yangilik_subSerializer

    def get_queryset(self):
        return Yangilik_sub.objects.all().order_by('-created_at')


@api_view(['GET', 'POST'])
def yangilik_sub_detail(request, pk):
    yangilik_sub = get_object_or_404(Yangilik_sub, pk=pk)

    if request.method == 'GET':
        yangilik_sub.view_count += 1
        yangilik_sub.save()
        serializer = Yangilik_subSerializer(yangilik_sub, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Foydalanuvchi tizimga kirmagan bo'lsa, AnonymousUser bo'lishi kerak
            if isinstance(request.user, AnonymousUser):
                # Anonim foydalanuvchini yaratish yoki olish
                anonymous_user, created = User.objects.get_or_create(username='anonymous')  # Anonim foydalanuvchini olish yoki yaratish
                serializer.save(user=anonymous_user, yangilik_sub=yangilik_sub)
            else:
                serializer.save(user=request.user, yangilik_sub=yangilik_sub)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)