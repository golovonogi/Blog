from django.db.models import Q
from django.views.generic import ListView

from blog.mixins import CatApiMixin
from blog.models import Post


class SearchView(CatApiMixin, ListView):
    model = Post
    template_name = 'search/search_index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return object_list

