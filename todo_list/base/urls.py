from .views import TaskList,TaskDetail
from django.urls import path

urlpatterns = [
    path("",TaskList.as_view(), name='tasks'),
    path("task/<int:pk>/",TaskDetail.as_view(), name = 'task'),
]
