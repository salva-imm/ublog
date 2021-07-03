from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user.api.v1.views import GetUserView


app_name = "user"
urlpatterns = [
    path('', GetUserView.as_view(), name='get_users'),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
