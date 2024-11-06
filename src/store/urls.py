from django.urls import path, include
from .views import get_store

urlpatterns = [path("", get_store, name="store")]
