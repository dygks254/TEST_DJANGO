from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
  title = serializers.CharField()
  content = serializers.TextField()

  def create(self, validated_data):
    return Article.objects.create(**validated_data)

  def update(self, instance, validated_data):
      instance.title = validated_data.get('title', instance.title)
      instance.content = validated_data.get('content', instance.content)
      instance.save()
      return instance