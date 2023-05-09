from django.contrib import admin

from apps.user import models


@admin.register(models.Article)
class ArticleModelAdmin(admin.ModelAdmin):

    list_display = ["title", "create_at"]


@admin.register(models.ArticleCategory)
class ArticleCategoryModelAdmin(admin.ModelAdmin):
    pass
