from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from .models import News, Category, Comment, Sud, Jurnalistik, Yangilik_sub

from rest_framework import filters, status
from rest_framework.response import Response

from .serializers import CategorySerializer, NewsSerializer, CommentSerializer, SudSerializer, JurnalistikSerializer, \
    Yangilik_subSerializer


class CategoryListView(ListAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


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
        return News.objects.all()


@api_view(['GET', 'POST'])
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)

    news.view_count += 1
    news.save()

    if request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, news=news)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Autentifikatsiya malumotlari taqdim etilmagan.'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = NewsSerializer(news)
    return Response(serializer.data)




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
        return Sud.objects.all()


@api_view(['GET', 'POST'])
def sud_detail(request, pk):
    sud = get_object_or_404(Sud, pk=pk)

    sud.view_count += 1
    sud.save()

    if request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, sud=sud)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Autentifikatsiya malumotlari taqdim etilmagan.'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = SudSerializer(sud)
    return Response(serializer.data)


class JurnalistikListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = JurnalistikSerializer

    def get_queryset(self):
        return Jurnalistik.objects.all()


@api_view(['GET', 'POST'])
def jurnalistik_detail(request, pk):
    jurnalistik = get_object_or_404(Jurnalistik, pk=pk)

    jurnalistik.view_count += 1
    jurnalistik.save()

    if request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, jurnalistik=jurnalistik)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Autentifikatsiya malumotlari taqdim etilmagan.'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = JurnalistikSerializer(jurnalistik)
    return Response(serializer.data)


class Yangilik_subListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Yangilik_subSerializer

    def get_queryset(self):
        return Yangilik_sub.objects.all()


@api_view(['GET', 'POST'])
def yangilik_sub_detail(request, pk):
    yangilik_sub = get_object_or_404(Yangilik_sub, pk=pk)

    yangilik_sub.view_count += 1
    yangilik_sub.save()

    if request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, yangilik_sub=yangilik_sub)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Autentifikatsiya malumotlari taqdim etilmagan.'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = Yangilik_subSerializer(yangilik_sub)
    return Response(serializer.data)