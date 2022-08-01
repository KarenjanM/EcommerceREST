from django.urls import path
from rest_framework import routers
from .views import ProductViewSet, search


router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('search/', search)
]
