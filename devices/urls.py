from django.urls import path
from .views import Status, Health


urlpatterns = [
    path('devicestatus/', Status.as_view()),
    path('devicestatus/health', Health.as_view()),
]
