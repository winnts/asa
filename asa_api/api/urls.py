from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'currency', views.CurrencyViewSet, basename='currency')
urlpatterns = router.urls
