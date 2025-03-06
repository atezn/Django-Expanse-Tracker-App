from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book'),
    path('chart-data/', views.chart_data, name='chart-data'),
]