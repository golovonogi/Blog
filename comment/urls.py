from django.urls import path
from . import views

app_name = 'comment'

urlpatterns=[
    path('post/<int:pk>/comment', views.NewCommentAddView.as_view(), name='comments'),
    path('post/<int:pk>/comment/edit_comment', views.CommentUpdateView.as_view(), name='commentsupdate'),
    path('post/<int:pk>/comment/delete_comment', views.CommentDeleteView.as_view(), name='commentsdelete'),
]
