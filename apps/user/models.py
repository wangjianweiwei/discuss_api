from django.db import models

from common.db.models import BaseModel
from common.db.fields import FlexibleForeignKey


class User(BaseModel):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)


class ArticleCategory(BaseModel):
    title = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class Article(BaseModel):
    title = models.CharField(max_length=32)
    category = FlexibleForeignKey(to="ArticleCategory")
    content = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
