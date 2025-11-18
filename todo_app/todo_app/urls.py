from django.urls import path
from task import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Single page: list + create
    path('', views.TodoListView.as_view(), name='todo_list'),

    # Update/Delete/Complete
    path('<int:id>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:id>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:id>/complete/', views.TodoCompleteView.as_view(), name='todo_complete'),
]
