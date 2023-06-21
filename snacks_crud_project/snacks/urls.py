from django.urls import path
from . import views

urlpatterns=[
    path('', views.Home.as_view(), name='home'),
    path('snacks/', views.SnackListView.as_view() , name="snacks"),
    path('<int:pk>/',views.SnackDetailView.as_view() , name='detailview'),
    path('create/', views.SnackCreateView.as_view() , name='create_snack'),
    path('<int:pk>/update/',views.SnackUpdateView.as_view() , name='update_snack'),
    path('<int:pk>/delete/', views.SnackDeleteView.as_view(), name='delete_snack')
    
]