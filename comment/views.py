from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView

from blog.mixins import CatApiMixin
from blog.models import Post
from comment.forms import CommentForm
from comment.models import Comment


class NewCommentAddView(CatApiMixin, LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = "comment/comment.html"

    def get_context_data(self, **kwargs):
        context = super(NewCommentAddView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        comments = form.save(commit=False)
        comments.author_comment = self.request.user
        comments.post = post
        comments.save()
        return super(NewCommentAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk':self.kwargs['pk']})

class CommentUpdateView(CatApiMixin, LoginRequiredMixin, UpdateView):
    form_class = CommentForm
    model = Comment
    template_name = "comment/comment_edit.html"

    def dispatch(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        self.text = comment.post.pk
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(CommentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.text})


class CommentDeleteView(CatApiMixin, LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment/item_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        self.text = comment.post.pk
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.text})

