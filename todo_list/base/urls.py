from .views import TaskList,TaskDetail,TaskCreate
from django.urls import path

urlpatterns = [
    path("",TaskList.as_view(), name='tasks'),
    path("task/<int:pk>/",TaskDetail.as_view(), name = 'task'),
    path("task-create/",TaskCreate.as_view(), name='task-create'),
]
