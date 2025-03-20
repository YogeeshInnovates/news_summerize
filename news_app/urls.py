
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_view, name='news_view'),
    path('news_audio/', views.news_audio, name='news_audio'),  # ✅ Add this line
    #  path("", views.text_to_speech_api, name="text_to_speech_api"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])