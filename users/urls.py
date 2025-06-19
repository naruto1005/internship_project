from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('protected/', views.protected_view),
]
