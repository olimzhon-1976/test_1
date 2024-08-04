
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    re_path(r'^news/.*$', views.news, name='news_fallback'),
    path('management/', views.management, name='management'),
    re_path(r'^management/.*$', views.management, name='management_fallback'),
    path('facts/', views.facts, name='facts'),
    re_path(r'^facts/.*$', views.facts, name='facts_fallback'),
    path('contacts/', views.contacts, name='contacts'),
    re_path(r'^contacts/.*$', views.contacts, name='contacts_fallback'),
    path('history/', views.history, name='history'),
    path('history/people', views.history_people, name='history'),
    path('history/photos', views.history_photos, name='history'),
]