from django.urls import path
from .views import index

app_name="musicapp"
urlpatterns = [
    path("", index, name="index"),
]