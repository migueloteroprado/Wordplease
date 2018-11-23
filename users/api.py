from django.contrib.auth.models import User
from rest_framework.viewsets import mixins, GenericViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer


class UsersViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    queryset = User.objects.all()
    permission_classes = [UserPermission]
    ordering = ['id']

    def get_serializer_class(self):
        return UserListSerializer if self.action == 'list' else UserSerializer

