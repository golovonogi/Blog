from django.views.generic.base import ContextMixin
from mysite.api.api import catapi, rubapi, kanyeapi


class KanyeApiMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kanye'] = kanyeapi()
        return context


class CatApiMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = catapi()
        return context

