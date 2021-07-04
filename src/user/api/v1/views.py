from rest_framework import status
from utils.permissions import IsGet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from user.api.v1.serializers import (
    UserSerializer,
    UserRegisterSerializer
)

User = get_user_model()


class GetUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    get_args = "user.view_user"
    permission_classes = [IsGet]


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        data = UserRegisterSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data = data.validated_data
        User.objects.create_user(
            email=data.get('email'),
            password=data.get('password')
        )
        # TODO: send email for activation
        return Response(status=status.HTTP_201_CREATED)


class UserActivateView:
    pass
