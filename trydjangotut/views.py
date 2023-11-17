from django.shortcuts import render
from .settings import ( INSTALLED_APPS )

def root_view(request):
  all_apps = {
    "articles": {
      'app_name': 'Blog App',
      'app_link': '/articles/'
    }
  }
  
  context = {
    'apps': all_apps
  }
  return render(request,'projectroot/root.html',context=context)