from django.urls import path, include
from django.contrib.auth import views as auth_views
from graphene_django.views import GraphQLView

from . import views
from rest_framework import routers

from .schema import schema

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'zones', views.ZoneViewSet)
router.register(r'tours', views.TourViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    # Rutas para la url /api/
    path("api/", include(router.urls)),
    # Rutas para la autenticación url /api/auth/
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),

    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/login"), name="logout"),
]
