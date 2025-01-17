from rest_framework import serializers
from apiapp.models import Article, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields='__all__'



