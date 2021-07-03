from utils.permissions import IsGet
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from user.api.v1.serializers import UserSerializer

User = get_user_model()


class GetUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    get_args = "user.view_user"
    permission_classes = [IsGet]
