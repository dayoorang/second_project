from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import hello_world, AccountCreateView

app_name = 'first_app'
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),

    path('login/', LoginView.as_view(template_name = 'accountsapp/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='accountsapp/logout.html'),
         name='logout')
]