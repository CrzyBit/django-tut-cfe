from django.contrib import admin
from django.urls import path, include
from .views import root_view
import articles

urlpatterns = [
  path('', root_view),
  path('articles/', include('articles.urls')),
  path('admin/', admin.site.urls),
]
