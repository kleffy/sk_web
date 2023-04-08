from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsArticleListView.as_view(), name='news_list'),
    path('<int:pk>/', views.NewsArticleDetailView.as_view(), name='news_detail'),
]
