from rest_framework import serializers
from store.models import Game,Category


class GameSerializer(serializers.Serializer):
    game_name = serializers.CharField(source='name', max_length=100)
    game_release_date = serializers.DateField(source='release_date')
    price = serializers.DecimalField(decimal_places=2, max_digits=6)
    description = serializers.CharField()
    category = serializers.CharField(source='category.title', max_length=100)
    slug = serializers.SlugField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'description')
