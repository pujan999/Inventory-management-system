import  django_filters
from .models import *

class PurchaseFilter(django_filters.FilterSet):
    release_year = django_filters.NumberFilter(field_name='date', lookup_expr='year')
    release_year__gt = django_filters.NumberFilter(field_name='date', lookup_expr='year__gt')
    
    
    class Meta:
        product = Purchase
        fields =['date']
                
        