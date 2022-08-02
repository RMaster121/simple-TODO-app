from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register(r'todo-items', views.TodoItemViewSet, basename='todo-items')
router.register(r'list-items', views.ListItemViewSet, basename='list-items')

urlpatterns = router.urls