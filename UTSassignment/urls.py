from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('initiate-chat/', include('chat.urls')),  # Include URLs for initiating chats
    path('signup/', include('users.urls')),  # Include URLs for user registration
    path('login/', include('users.urls')),  # Include URLs for user login
]
