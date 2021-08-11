
from django.urls import path, include

from commentapp.views import CommentCreationView, CommentDeleteView

app_name = 'commentapp'
urlpatterns = [
    path('create/', CommentCreationView.as_view(), name = 'create'),
    path('delete/', CommentDeleteView.as_view(), name='delete'),

]