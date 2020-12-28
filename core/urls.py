from django.urls import path, re_path
from . import views

app_name = "core"
urlpatterns = [
    path('',views.HomeListView.as_view(), name="home"),
    path('home/',views.HomeListView.as_view(), name="home"),
    re_path(r'^(?P<slug>.*)/$',views.BlogDetailView.as_view(), name="blog-detail"),
    re_path(r'^(?P<blog_id>\d+)/$',views.BlogDetailView.as_view(), name="blog-detail")
]
