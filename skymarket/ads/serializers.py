from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'text', 'ad',)


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'price', 'image', 'description', 'user',)


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'price', 'image', 'description', 'user',)
