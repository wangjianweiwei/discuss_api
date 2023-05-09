from django.urls import path, re_path

from apps.user import views

urlpatterns = [
    path("articles", views.ArticleListView.as_view()),
    path("article/<str:pk>", views.ArticleView.as_view())
]
