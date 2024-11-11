# base/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
router.register(r'startups', views.StartupProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),                     # Register user and startup endpoints
    path('api/search_startups/', views.search_startups, name='search_startups'),  # Custom search API
    # Other routes can be added here as needed
]
