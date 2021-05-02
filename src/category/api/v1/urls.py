from .views import CategoriesView
from django.urls import path


app_name = "category"
urlpatterns = [
    path('', CategoriesView.as_view(), name='categories-get-create'),
]
