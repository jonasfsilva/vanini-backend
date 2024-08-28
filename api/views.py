from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import viewsets
from catalog.models import Category, Product, ProductGalery
from configs.models import BannerHeader, BannerMid, GaleryTypeVideo, Site
from configs.models import Contact
from configs.models import DinamicTool
from configs.models import MenuItem
from configs.models import NewsLetterLead
from configs.models import Galery
from api.serializers import (
    BannerHeaderSerializer,
    BannerMidSerializer,
    CategorySerializer,
    ContactSerializer,
    DinamicToolSerializer,
    GalerySerializer,
    GaleryVideoSerializer,
    MenuItemSerializer,
    NewsLetterLeadSerializer,
    PostSerializer,
    ProductGalerySerializer,
    ProductSerializer,
    QuotationInfoSerializer,
    SiteSerializer,
    StateSerializer,
)
from location.models import State
from orders.models import QuotationInfo
from posts.models import Post


class SiteModelViewSet(viewsets.ModelViewSet):

    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    http_method_names = [
        "get",
    ]


class ContactModelViewSet(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    http_method_names = ["get", "post"]


class DinamicToolModelViewSet(viewsets.ModelViewSet):

    serializer_class = DinamicToolSerializer
    queryset = DinamicTool.objects.all()
    http_method_names = [
        "get",
    ]


class MenuItemModelViewSet(viewsets.ModelViewSet):

    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    http_method_names = [
        "get",
    ]


class GaleryModelViewSet(viewsets.ModelViewSet):

    serializer_class = GalerySerializer
    queryset = Galery.objects.all()
    http_method_names = [
        "get",
    ]


class GaleryTypeVideoModelViewSet(viewsets.ModelViewSet):

    serializer_class = GaleryVideoSerializer
    queryset = GaleryTypeVideo.objects.all()
    http_method_names = [
        "get",
    ]


class NewsLetterLeadModelViewSet(viewsets.ModelViewSet):

    serializer_class = NewsLetterLeadSerializer
    queryset = NewsLetterLead.objects.all()
    http_method_names = ["get", "post"]


class PostModelViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = [
        "get",
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "slug",
    ]


class BannerHeaderModelViewSet(viewsets.ModelViewSet):

    serializer_class = BannerHeaderSerializer
    queryset = BannerHeader.objects.all()
    http_method_names = [
        "get",
    ]


class BannerMidModelViewSet(viewsets.ModelViewSet):

    serializer_class = BannerMidSerializer
    queryset = BannerMid.objects.all()
    http_method_names = [
        "get",
    ]


class StateViewSet(viewsets.ModelViewSet):

    serializer_class = StateSerializer
    queryset = State.objects.all()
    http_method_names = [
        "get",
    ]


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = [
        "get",
    ]


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = [
        "get",
    ]


class ProductGaleryViewSet(viewsets.ModelViewSet):

    serializer_class = ProductGalerySerializer
    queryset = ProductGalery.objects.all()
    http_method_names = [
        "get",
    ]


class QuotationInfoViewSet(viewsets.ModelViewSet):

    serializer_class = QuotationInfoSerializer
    queryset = QuotationInfo.objects.all()
    http_method_names = [
        "get",
        "post",
    ]


def index(request):
    return render(request, "index.html", {})
