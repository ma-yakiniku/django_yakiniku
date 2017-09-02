from django.conf.urls import url
from ioyapp import views

urlpatterns = [
    # 書籍
    url(r'^index/$', views.index, name='index'),   # 一覧
    url(r'^cap/$', views.cap, name="cap"),
    #url(r'^book/$', views.book_list, name='book_list'),   # 一覧

]\
