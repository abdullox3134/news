from django.urls import path

from new.views import CategoryListView, categorydetail, NewsListView, news_detail, SudListView, sud_detail, \
    JurnalistikListView, jurnalistik_detail, Yangilik_subListView, yangilik_sub_detail

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', categorydetail, name='category_detail'),

    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),

    path('sud/', SudListView.as_view(), name='sud_list'),
    path('sud/<int:pk>/', sud_detail, name='sud_detail'),

    path('jurnalistik/', JurnalistikListView.as_view(), name='jurnalistik_list'),
    path('jurnalistik/<int:pk>/', jurnalistik_detail, name='jurnalistik_detail'),

    path('yangilik_sub/', Yangilik_subListView.as_view(), name='yangilik_sub_list'),
    path('yangilik_sub/<int:pk>/', yangilik_sub_detail, name='yangilik_sub_detail'),
]

