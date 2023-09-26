from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from api import serializers
from api.models import Post


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostList(APIView):
    authentication_classes = []
    serializer_class = serializers.PostSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        queryset = Post.objects.all()
        return Response(data={'queryset': self.serializer_class(queryset, many=True).data,
                              }, status=200)

    def post(self, request):
        post_data = Post.objects.create(title=request.data['title'], body=request.data['body'],author=self.request.user)
        post_data.save()
        return Response(status=200)


class BlogListView(ListView):
    queryset = Post.objects.all()
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        latest_blog = Post.objects.all().first()
        context['latest_blog'] = latest_blog
        context['blogs'] = Post.objects.all()
        return context


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer



