from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.dishes.api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users_ration', views.UserRationViewSet)
router.register(r'ration_dishes', views.RationDishViewSet)
router.register(r'dishes', views.DishViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
