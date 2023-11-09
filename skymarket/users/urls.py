from django.urls import include, path
from djoser.views import UserViewSet, TokenCreateView
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig


app_name = UsersConfig.name

users_router = SimpleRouter()

users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(users_router.urls)),
]

