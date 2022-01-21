from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('article/', include([
        path('', views.articles_list, name="article_list"),
        re_path('^(?P<year>\d{4})/', views.articles_year, name='articles_year'),
        re_path('^(?P<month>\d{4})/', views.articles_month, name="articles_month"),
        re_path('^(?P<article_id>\S{10,})/', views.articles_detail, name="articles_detail"),
        path('<uuid:author_id>', views.articles_author, name="articles_author"),
        path('<uuid:author_id>', views.articles_liked, name="articles_liked"),
        path('<uuid:author_id>', views.articles_collected, name="articles_collected"),
    ]
    ))
]
