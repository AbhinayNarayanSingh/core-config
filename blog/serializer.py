from rest_framework import serializers
from .models import *


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = ["user"]


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ["name"]


class PostsSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    # tags = TagsSerializer(many=True)
    # comments = CommentsSerializer(many=True)

    class Meta:
        model = Posts
        fields = '__all__'

    
    def get_tags(self, obj):
        items = obj.tags_set.all()
        serializer = TagsSerializer(items, many=True)
        return serializer.data

    def get_likes(self, obj):
        items = obj.likes_set.all()
        serializer = LikesSerializer(items, many=True)
        return serializer.data