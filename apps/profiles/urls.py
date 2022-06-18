from django.urls import path

from .views import (AgentsListAPIView, ProfileDetailAPIView, TopAgentsListAPIView,
                    ProfileUpdateAPIView)

urlpatterns = [
    path("me/", ProfileDetailAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", ProfileUpdateAPIView.as_view(), name="update_profile"
    ),
    path("agents/all/", AgentsListAPIView.as_view(), name="all-agents"),
    path("top-agents/all/", TopAgentsListAPIView.as_view(), name="top-agents"),
]
