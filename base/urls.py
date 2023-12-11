from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, logout_View, RegisterPage


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', logout_View, name = 'logout'),
    path('register/', RegisterPage.as_view(), name = 'register'),
    
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreate.as_view(), name ='task-create'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(), name ='task-update'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(), name ='task-delete'),
   
]