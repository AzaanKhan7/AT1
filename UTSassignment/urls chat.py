from django.urls import path
from .views import send_message_view, index

urlpatterns = [
    path('', index, name='index'),  # URL pattern for displaying the chat interface
    path('send-message/', send_message_view, name='send_message'),  # URL pattern for sending messages
]
