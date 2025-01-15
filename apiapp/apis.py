from rest_framework import viewsets, routers
from apiapp.models import Article
from apiapp.serializers import Articleserializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Articleserializer


router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)