from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewset

router = DefaultRouter()
router.register(r'posts', PostViewset, basename='posts')

urlpatterns = [
    path('', PostViewset.as_view({'get': 'get_posts', 'post':'create_post'}), name='posts'),
] + router.urls
