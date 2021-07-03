from .views import GetCategoriesView
from django.urls import path


app_name = "category"
urlpatterns = [
    path('', GetCategoriesView.as_view(), name='categories-get-create'),
]
