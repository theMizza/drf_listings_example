from django.urls import path
from .views import ListingApiView, CategoriesApiView, ListingsApiView, CategoryApiView, CreateListingApiViev, \
    CreateCategoryApiViev, UsersListingsView


urlpatterns = [
    path('all/', ListingsApiView.as_view()),
    path('my/', UsersListingsView.as_view()),
    path('<int:pk>/', ListingApiView.as_view()),
    path('create/', CreateListingApiViev.as_view()),
    path('categories/all/', CategoriesApiView.as_view()),
    path('categories/<int:pk>/', CategoryApiView.as_view()),
    path('categories/create/', CreateCategoryApiViev.as_view())
]
