from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('property/create/', views.property_create_with_unit, name='create_property_with_unit'),
    path('property/<int:property_id>', views.property_units_list, name='property_units'),

    path('property/units/create/<int:property_id>', views.unit_create, name='unit_create'),
    path('property/units/<int:pk>/update/', views.unit_update, name='unit_update'),
    path('property/units/<int:pk>/delete/', views.unit_delete, name='unit_delete'),

    path('tenant', views.tenant_list, name='tenant_list'),
    path('tenant/details/<int:pk>', views.tenant_detail, name='tenant_detail'),
    path('tenant/create/', views.create_tenant, name='create_tenant'),


]
