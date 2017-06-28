# Create your views here.
from django.shortcuts import render
from open_news.models import Article, NewsWebsite


def home(request):
    categories = NewsWebsite.objects.all()
    news = Article.objects.order_by('-checker_runtime', '-date')
    top_news = Article.objects.order_by('-views')
    return render(request, 'open_news/index.html', {'news': news, 'top_news': top_news, 'categories': categories})


def news_details(request, id):
    categories = NewsWebsite.objects.all()
    top_news = Article.objects.order_by('-views')[:5]
    news_detail = Article.objects.get(id=id)
    news_detail.views = news_detail.views + 1
    news_detail.save()
    return render(request, 'open_news/news_details.html', {'news_detail': news_detail, 'top_news': top_news, 'categories': categories})