from django.http import HttpResponse, JsonResponse

from blog.models import Post
from blog.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


def serve_test(request):
    return HttpResponse("XDDDD")


def get_all_posts(request):
    new_post = Post.objects.all()
    serializer = PostSerializer(new_post, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def add_new_post(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def update_post(request, id_post):
    try:
        post_object = Post.objects.get(id=id_post)
    except Post.DoesNotExist:
        return HttpResponse('Błąd serwera!', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_post = PostSerializer(post_object)
        return JsonResponse(serializer_post.data)
