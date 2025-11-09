from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    # path('', views.index, name="tasks"),
    path('', views.TaskListView.as_view(), name="all"),
    path('add/', views.TaskCreateView.as_view(), name="add"),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name="delete"),
    path('complete/<int:pk>/', views.TaskCompleteView.as_view(), name='complete'),
]
