from rest_framework import serializers
from chat.models import Chat, ChatInfo, ChatMessage, Client
from configs.models import Activity, BannerHeader, BannerMid, GaleryTypeVideo, Site
from configs.models import Contact
from configs.models import DinamicTool
from configs.models import MenuItem
from configs.models import NewsLetterLead
from configs.models import Galery
from posts.models import Post
from quiz.models import Answer, Question, Quiz


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


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        return AnswerSerializer(obj.answer_set.all(), many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ChatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatInfo
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = '__all__'
    

class ChatMessageSerializer(serializers.ModelSerializer):

    answer = serializers.SerializerMethodField()
    # reply = ReplySerializer(required=False, allow_null=True)

    class Meta:
        model = ChatMessage
        fields = '__all__'
        
    def get_answer(self, obj):
        return ReplySerializer(obj.answer).data


class ChatSerializer(serializers.ModelSerializer):

    messages = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = '__all__'

    def get_messages(self, obj):
        return ChatMessageSerializer(obj.messages.all(), many=True).data
