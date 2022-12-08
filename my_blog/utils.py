from .models import *
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Count

class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = cache.get('cats')
        # if not cats:
        #     cats = Category.objects.annotate(Count("myblog"))
        #     cache.set('cats', cats, 60 )
        cats = Category.objects.all()
        context['cats'] = cats
        return context 

        