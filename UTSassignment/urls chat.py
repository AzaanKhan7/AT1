from django.urls import path, include
from .views import send_message_view, index  # Import the index view

urlpatterns = [
    path('send-message/', send_message_view, name='send_message'),
    path("", index, name="index"),  # Add the index view URL pattern
    path('hello/', include("hello.urls")),
]
