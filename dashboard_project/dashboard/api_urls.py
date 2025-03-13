from django.urls import path
from . import api_views

urlpatterns = [
    path('items/', api_views.get_items, name='api-items-list'),
    path('items/<int:item_id>/', api_views.get_item, name='api-item-detail'),
    path('items/add/', api_views.add_item, name='api-item-add'),
    path('items/update/<int:item_id>/', api_views.update_item, name='api-item-update'),
] 