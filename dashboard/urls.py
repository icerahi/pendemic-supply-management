from django.urls.conf import path
from .views.dashboard import DashboardView
from .views.requests import ReqeustListCreateView
from .views.equipments import EquipmentListView
from .views.calculate import CalculateView
from .views.articles import ArticleListView

urlpatterns=[
    path('',DashboardView.as_view(),name='dashboard'),
    path('requests/',ReqeustListCreateView.as_view(),name='requests'),
    path('equipments/',EquipmentListView.as_view(),name='equipments'),
    path('calculate/',CalculateView.as_view(),name='calculate'),
    path('articles/',ArticleListView.as_view(),name='articles'),
    ]