from django.views.generic import ListView, DetailView
from .models import NewsArticle

class NewsArticleListView(ListView):
    model = NewsArticle
    template_name = 'news/newsarticle_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = ['-pub_date']

class NewsArticleDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/newsarticle_detail.html'
    context_object_name = 'article'
