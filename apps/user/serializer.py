# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/5/5 22:05
"""
from rest_framework import serializers

from apps.user import models


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleCategory
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(required=False)

    class Meta:
        model = models.Article
        fields = "__all__"
        extra_kwargs = {'title': {'required': False}}
