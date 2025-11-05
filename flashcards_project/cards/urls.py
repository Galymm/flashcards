from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_card, name='add_card'),
    path('edit/<int:card_id>/', views.edit_card, name='edit_card'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('add_subcategory/<int:parent_id>/', views.add_category, name='add_subcategory'),
]
