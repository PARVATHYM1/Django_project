from.import views
from django.urls import path
from django.views.generic import RedirectView



urlpatterns = [
     path('login',views.loginadmin, name='login'),
     path('', RedirectView.as_view(url='login')),
     path('adminlogout', views.logoutadmin, name='adminlogout'),
     path('dashboard', views.admindashboard, name='admindashboard'),
     ]