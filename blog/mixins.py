from django.views.generic.base import ContextMixin
from mysite.api.api import catapi, rubapi, kanyeapi


class CatApiMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = catapi()
        context['eur'] = rubapi()
        context['kanye'] = kanyeapi()
        return context


