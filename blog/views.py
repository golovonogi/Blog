from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from blog.mixins import CatApiMixin
from .models import Post
from django.utils import timezone
from .forms import PostForm


class PostListView(CatApiMixin, ListView):
    model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginate_by = 10


class PostDetailView(CatApiMixin, DetailView):
    model = Post


class PostNewView(CatApiMixin, LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "blog/post_edit.html"
    model = Post

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return super(PostNewView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_list')


class PostEditView(CatApiMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    model = Post

    def form_valid(self, form):
        form.save()
        return super(PostEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk':self.object.pk})


class PostDeleteView(CatApiMixin, LoginRequiredMixin, DeleteView):
    success_url = "/"
    model = Post
    template_name = 'blog/item_confirm_delete.html'




