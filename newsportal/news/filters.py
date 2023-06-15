import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    date = django_filters.DateFilter(field_name='dateCreate',
                                     lookup_expr='gt',
                                     label='Date',
                                     widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
            'dateCreation': ['gt'],
        }
