from django.db import models
from rest_framework import serializers
from mysic_blog.models import Post
from mysic_blog.forms import PostForm
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True) #May to Many fields to see the name

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'post_date', 'likes')

        # title = serializers.CharField(max_length=255)
        # title_tag = serializers.CharField(max_length=255, default='Casmena')
        # author = serializers.CharField(User)
        # body = serializers.CharField(blank=True, null=True)
        # post_date = serializers.CharField(auto_now_add=True)
        # likes = serializers.CharField(User, related_name='blog_posts')

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.title_tag = validated_data.get('title_tag', instance.title_tag)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.post_date = validated_data.get('post_date', instance.post_date)
    #     instance.likes = validated_data.get('likes', instance.likes)
    #     instance.save()
    #     return instance


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)  # May to Many fields to see the name

    class Meta:
        model = Post
        exclude = ('title_tag',)


class AddPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
