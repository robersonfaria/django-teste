from django.urls import path
from .views import home
from .views import produto

urlpatterns = [
    path('', home),
    path('produto/<int:id>', produto)
]
