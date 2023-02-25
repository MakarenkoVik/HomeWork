from rest_framework import serializers
from store.models import Game,Category


class GameSerializer(serializers.Serializer):
    game_name = serializers.CharField(source='name', max_length=100)
    game_release_date = serializers.DateField(source='release_date')
    price = serializers.DecimalField(decimal_places=2, max_digits=6)
    description = serializers.CharField()
    category = serializers.CharField(source='category.title', max_length=100)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Game(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('game_name', instance.name)
        instance.release_date = validated_data.get('game_release_date', instance.release_date)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.slug = validated_data.get('slug', instance.slug)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'description')

