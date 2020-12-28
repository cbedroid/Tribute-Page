from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView,View
from .models import Blog


class HomeListView(ListView):
    model = Blog
    template_name = "core/index.html"
    context_object_name = "blogs"

    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "core/blog_detail.html"
    pk_url_kwarg = "blog_id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

   