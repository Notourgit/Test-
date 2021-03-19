from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Book

class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(name__icontains=query) | Q(author__icontains=query)
        )
        return object_list