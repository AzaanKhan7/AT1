from django.urls import path
from .views import user_registration_view

urlpatterns = [
    path('signup/', user_registration_view, name='user_registration'),  # URL pattern for user registration
]
