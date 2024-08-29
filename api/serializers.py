from rest_framework import serializers
from catalog.models import Category, Model, Product, ProductGalery
from configs.models import Activity, BannerHeader, BannerMid, GaleryTypeVideo, Site
from configs.models import Contact
from configs.models import DinamicTool
from configs.models import MenuItem
from configs.models import NewsLetterLead
from configs.models import Galery
from location.models import State
from orders.models import QuotationInfo
from posts.models import Post


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
        # fields = ['id', 'account_name', 'users', 'created']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class DinamicToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = DinamicTool
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class GalerySerializer(serializers.ModelSerializer):
    
    images = serializers.SerializerMethodField()

    class Meta:
        model = Galery
        fields = '__all__'

    def get_images(self, obj):
        return [img.image.url for img in obj.images.all()]


class GaleryVideoSerializer(serializers.ModelSerializer):

    videos = serializers.SerializerMethodField()

    class Meta:
        model = GaleryTypeVideo
        fields = '__all__'

    def get_videos(self, obj):
        return [img.video_link.url for img in obj.videos.all()]


class NewsLetterLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterLead
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class BannerHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerHeader
        fields = '__all__'


class BannerMidSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerMid
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductGalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGalery
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_images(self, obj):
        return ProductGalerySerializer(obj.images, many=True).data


class QuotationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationInfo
        fields = '__all__'
