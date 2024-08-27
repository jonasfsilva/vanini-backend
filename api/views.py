import requests
import base64
from api.services.chatgpt_service import chatgpt_send_message, get_previous_context
from chat.models import Chat, ChatInfo, ChatMessage, Client
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import redirect, render
from rest_framework import viewsets
from configs.models import Activity, BannerHeader, BannerMid, GaleryTypeVideo, Site
from configs.models import Contact
from configs.models import DinamicTool
from configs.models import MenuItem
from configs.models import NewsLetterLead
from configs.models import Galery
from api.serializers import ActivitySerializer, AnswerSerializer, BannerHeaderSerializer, BannerMidSerializer, ChatInfoSerializer, ChatMessageSerializer, ChatSerializer, ClientSerializer, DinamicToolSerializer, GalerySerializer, GaleryVideoSerializer, MenuItemSerializer, NewsLetterLeadSerializer, PostSerializer, QuestionSerializer, QuizSerializer, SiteSerializer
from api.serializers import ContactSerializer
from posts.models import Post
from quiz.models import Answer, Question, Quiz


class SiteModelViewSet(viewsets.ModelViewSet):

    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    http_method_names = ['get', ]


class ContactModelViewSet(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    http_method_names = ['get', 'post']


class DinamicToolModelViewSet(viewsets.ModelViewSet):

    serializer_class = DinamicToolSerializer
    queryset = DinamicTool.objects.all()
    http_method_names = ['get', ]


class MenuItemModelViewSet(viewsets.ModelViewSet):

    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
    http_method_names = ['get', ]


class ActivityModelViewSet(viewsets.ModelViewSet):

    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    http_method_names = ['get', ]


class GaleryModelViewSet(viewsets.ModelViewSet):

    serializer_class = GalerySerializer
    queryset = Galery.objects.all()
    http_method_names = ['get', ]


class GaleryTypeVideoModelViewSet(viewsets.ModelViewSet):

    serializer_class = GaleryVideoSerializer
    queryset = GaleryTypeVideo.objects.all()
    http_method_names = ['get', ]


class NewsLetterLeadModelViewSet(viewsets.ModelViewSet):

    serializer_class = NewsLetterLeadSerializer
    queryset = NewsLetterLead.objects.all()
    http_method_names = ['get', 'post']


class PostModelViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = ['get', ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug',]


class BannerHeaderModelViewSet(viewsets.ModelViewSet):

    serializer_class = BannerHeaderSerializer
    queryset = BannerHeader.objects.all()
    http_method_names = ['get', ]


class BannerMidModelViewSet(viewsets.ModelViewSet):

    serializer_class = BannerMidSerializer
    queryset = BannerMid.objects.all()
    http_method_names = ['get', ]


class QuizModelViewSet(viewsets.ModelViewSet):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    http_method_names = ['get', ]


class QuestionModelViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    http_method_names = ['get', ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz',]


class AnswerModelViewSet(viewsets.ModelViewSet):

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    http_method_names = ['get', ]


class ClientModelViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    http_method_names = ['get', ]


class ChatInfoModelViewSet(viewsets.ModelViewSet):

    serializer_class = ChatInfoSerializer
    queryset = ChatInfo.objects.all()
    http_method_names = ['get', ]


class ChatModelViewSet(viewsets.ModelViewSet):

    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    http_method_names = ['get', 'post']


class ChatMessageModelViewSet(viewsets.ModelViewSet):

    serializer_class = ChatMessageSerializer
    queryset = ChatMessage.objects.all()
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['chat',]

    def perform_create(self, serializer):
        new_obj = serializer.save()

        previous_context = get_previous_context(new_obj.chat)
        response = chatgpt_send_message(new_obj.text, previous_context)

        chat_response = ChatMessage.objects.create(
            chat=new_obj.chat,
            text=response,
            type=ChatMessage.ASSISTANT
        )
        new_obj.answer = chat_response
        new_obj.save()
        return new_obj


def pdf_view(request):
    response = requests.get("https://jpprefeito-statics.nyc3.digitaloceanspaces.com/PLANO%20DE%20GOVERNO%20JOSIVALDO%20JP.pdf")
    pdf_content = base64.b64encode(response.content).decode()

    context = {
        "pdf": pdf_content,
    }

    return render(request, "pdf_page.html", context)


def index(request):
    return render(request, "index.html", {})
