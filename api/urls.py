from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register(r'todo-items', views.TodoItemViewSet, basename='todo-items')

urlpatterns = router.urls