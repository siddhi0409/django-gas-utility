from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_requests/', views.track_requests, name='track_requests'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('account/', views.account_info, name='account_info'),
   
]
