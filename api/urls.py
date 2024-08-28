# example/urls.py
from api import views
from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
   openapi.Info(
      title="Vanini API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'contacts', views.ContactModelViewSet, basename='contacts')
router.register(r'dinamic-tools', views.DinamicToolModelViewSet, basename='dinamic_tools')
router.register(r'menu-items', views.MenuItemModelViewSet, basename='menu_items')
router.register(r'galery-images', views.GaleryModelViewSet, basename='galery_images')
router.register(r'galery-videos', views.GaleryTypeVideoModelViewSet, basename='galery_videos')
router.register(r'news-letter', views.NewsLetterLeadModelViewSet, basename='news-letter')
router.register(r'posts', views.PostModelViewSet, basename='posts')
router.register(r'banners-main', views.BannerHeaderModelViewSet, basename='banners')
router.register(r'banners-down', views.BannerMidModelViewSet, basename='banners-mid')
router.register(r'sites', views.SiteModelViewSet, basename='sites')

router.register(r'states', views.StateViewSet, basename='states')
router.register(r'categorys', views.CategoryViewSet, basename='categorys')
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'quotations', views.QuotationInfoViewSet, basename='quotations')
router.register(r'products-categorys', views.CategoryViewSet, basename='products-categorys')

urlpatterns = router.urls

urlpatterns += [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

