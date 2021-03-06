from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ 
    User model serializer 
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        min_length=8, write_only=True,
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
