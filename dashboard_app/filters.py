# dashboard/filters.py
import django_filters
from .models import Search

class SearchFilter(django_filters.FilterSet):
    artist_name = django_filters.CharFilter(field_name='artist_name', lookup_expr='icontains', label='Artist Name')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains', label='Category')
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains', label='Country')

    class Meta:
        model = Search
        fields = ['artist_name', 'category', 'country']
