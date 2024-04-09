from django.urls import path
from .views import EmployeeAuthenticationView, ProductListCreateView, ProductRetrieveUpdateDestroyView, \
    CustomerListCreateView, CustomerRetrieveUpdateDestroyView

urlpatterns = [
    path('authenticate/', EmployeeAuthenticationView.as_view(), name='employee-authenticate'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<slug:slug>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
]
