from django.conf.urls import url
from open_news import views as v


urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^(?P<id>\d+)/$', v.news_details, name='news_details'),
]