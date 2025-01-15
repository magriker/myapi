from rest_framework import serializers
from apiapp.models import Article, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model = Article



