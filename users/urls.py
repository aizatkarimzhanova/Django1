from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.reqister_view),
    path('login/', views.auth_login_view),
    path('logout/', views.auth_logout_view),
]