import os
from uuid import uuid4

from django.conf import settings
from django.http.response import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView

from apps.user import models
from apps.user import serializer


class ArticleListView(ListAPIView):
    queryset = models.Article.objects.select_related("category")
    serializer_class = serializer.ArticleSerializer


class ArticleView(RetrieveUpdateAPIView):
    queryset = models.Article.objects
    serializer_class = serializer.ArticleSerializer


class ArticleMediaUploadView(APIView):

    @staticmethod
    def post(request):
        file: InMemoryUploadedFile = request.FILES.get("file[]")

        filename = f"{uuid4().hex}_{file.name}"
        with open(os.path.join(settings.MEDIA_ROOT, filename), "wb") as f:
            f.write(file.read())

        return JsonResponse({
            "msg": "",
            "code": 0,
            "data": {
                "errFiles": [],
                "succMap": {
                    filename: f"http://localhost:7777/media/{filename}"
                }
            }
        })
