from django.urls import path
from . import views

urlpatterns = [path('', views.PersonView.as_view(), name='index'),
               path('<int:pk>/', views.show_user, name='info')
               ]
