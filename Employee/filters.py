from django_filters import rest_framework as filters
from .models import Employee

class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    phone = filters.CharFilter(field_name='phone', lookup_expr='icontains')
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')
    salary = filters.RangeFilter(field_name='salary')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'address', 'salary']   