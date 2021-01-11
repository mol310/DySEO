from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('DySEO/SearchEngineOptimizer/', views.Crawling, name='searchengineoptimizer'),
    path('DySEO/SearchEngineOptimizer', views.Crawling, name='searchengineoptimizer'),
    path('DySEO/index/', views.index, name='index'),
    path('DySEO/index', views.index, name='index'),
    path('DySEO/history/', views.history, name='history'),
    path('DySEO/history', views.history, name='history'),
    path('DySEO/information/', views.information, name='information'),
    path('DySEO/information', views.information, name='information'),
    path('DySEO/resultpage', views.make_plot, name='make_plot'),
    path('DySEO/resultpage/', views.make_plot, name='make_plot'),
    path('DySEO/testpage/', views.test, name='test'),
    path('DySEO/testpage', views.test, name='test'),
]
