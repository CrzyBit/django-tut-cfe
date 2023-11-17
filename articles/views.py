from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Article
# Create your views here.

def index(request):
  article_objects = Article.objects.all()
  context = {
    'articles':article_objects
  }
  response = render_to_string('articles/index.html', context=context)
  return HttpResponse(response)

def detail(request, id):
  article_object = Article.objects.get(id=id)
  
  context = {
    'article_object': article_object
  }
  response = render_to_string('articles/detail.html', context=context)
  return HttpResponse(response)