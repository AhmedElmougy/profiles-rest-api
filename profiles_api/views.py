from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken


from profiles_api.serializers import UserSerializer
from profiles_api.permissions import UpdateOwnProfile


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    Authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, UpdateOwnProfile, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['username', 'email']


class UserLoginApiView(ObtainAuthToken):
    """
    Handle creating user authintication tokens 
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
