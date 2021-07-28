
from django.contrib import admin
from django.urls import path, include

from profileapp.views import ProfileCreationView, ProfileUpdateView

app_name = 'profileapp'
urlpatterns = [
    path('create/', ProfileCreationView.as_view(), name = 'create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')

]
