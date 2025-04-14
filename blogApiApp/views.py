from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# class BlogPostListCreate(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class BlogPostRetUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'pk'


@api_view(['GET'])
def index(req):
    return Response({'Success': "Setup was successful"})

@api_view(['GET', 'POST'])
def postsHandler(req):
    if req.method == 'GET':
        _posts =  Post.objects.all()
        print(_posts)
        serializer = PostSerializer(_posts, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        data = req.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success': 'The post was successfully created'}, status=201)
        else:
            return Response(serializer.errors, status=400)
        
@api_view(['GET', 'DELETE'])
def postHandler(req):
    post_id = req.data.get('post_id')
    if req.method == 'GET':
        pass
    elif req.method == 'DELETE':
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return Response({'Success': 'The post was deleted..'})
        except Post.DoesNotExist:
            return Response({'Err': 'Post does not exist'}, status=404)