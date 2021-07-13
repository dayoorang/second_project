from django.urls import path
from .views import hello_world

app_name = 'first_app'
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world')
    path('create/', AccountCreateView.as_view(), name='create')

]