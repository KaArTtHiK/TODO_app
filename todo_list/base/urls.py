from .views import TaskList
from django.urls import path

urlpatterns = [
    path("",TaskList.as_view(), name='tasks'),
]
