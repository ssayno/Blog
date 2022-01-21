__author__ = "Rifiuto"
__version__ = '1.0'

from django.urls import path, include
from . import views


app_name = 'author'
# 路由级连包含
urlpatterns = [
    path('author/', include([
        path('register/', views.author_registor, name='register'),
        path('login/', views.author_login, name='login'),
    ]
    ))
]