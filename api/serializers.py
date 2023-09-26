from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title','status','body','author','image','publication_date','category']

