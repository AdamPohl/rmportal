
from django.urls import path

from . import views

urlpatterns = [
    path('portal/', views.index, name='login'),
    path('user/auth', views.auth_view),
    path('register', views.register_user),
    path('create_user', views.create_user),
    path('logout', views.logout)
]