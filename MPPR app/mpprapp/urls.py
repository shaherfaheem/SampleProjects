from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.InsertPageView, name = "insertpage"),
    path("insert/", views.InsertData, name = "insert"),
    path('list/', views.GetData, name='list'),
    path('list/<int:pk>/', views.DeleteData, name = "delete"),
    path('update/<int:pk>/', views.Edit, name = 'update'),
    path('updated/<int:pk>/', views.EditData, name = 'updated'),
    path('filter/area', views.filterArea, name = 'filterArea'),
    path('filter/work', views.filterWorks, name = 'filterWorks'),
]
   