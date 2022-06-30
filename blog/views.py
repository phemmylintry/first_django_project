from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewset(viewsets.GenericViewSet):
    serializer_class = PostSerializer

    def get_posts(self, request):
        queryset = Post.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def create_post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)