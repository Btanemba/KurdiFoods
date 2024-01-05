from django.urls import path
from core.views import index, about, contact
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', views.login_admin, name='login'),
    path('logout/', views.logout_admin, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard')

]
