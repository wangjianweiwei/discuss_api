from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from apps.user import models
from apps.user import serializer


class ArticleListView(ListAPIView):
    queryset = models.Article.objects.select_related("category")
    serializer_class = serializer.ArticleSerializer


class ArticleView(RetrieveUpdateAPIView):
    queryset = models.Article.objects
    serializer_class = serializer.ArticleSerializer




# def ArticleContentView(request):
#     from django.http.response import JsonResponse
#     id = request.GET.get("id")
#     return JsonResponse([{"insert": id}], safe=False)
#
#
# def ArticleSaveView(request):
#     from django.http.response import JsonResponse
#     import json
#     print(json.loads(request.body))
#     return JsonResponse([{"insert": 123}], safe=False)
