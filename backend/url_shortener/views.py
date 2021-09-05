from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from url_shortener.models import CustomURL
from url_shortener.serializer import CustomURLCreateSerializer, CustomURLSerializer
from url_shortener.utils import get_unique_id, encode_base62, decode_base62


class CustomURLViewset(viewsets.ModelViewSet):
    queryset = CustomURL.objects.all()
    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        print("Action: ", self.action)
        if self.action == "create":
            return CustomURLCreateSerializer
        return CustomURLSerializer

    def create(self, request):
        print("Hello: ", self.action)
        serializer = self.get_serializer()
        print(serializer)
        return Response({"output": "Hello World"})


class ShortenURL(APIView):
    """
    post: shorten a given long url
    """

    def post(self, request, format=None):
        long_url = request.data.get("long_url", None)
        if long_url:
            custom_url = CustomURL.url_exists(long_url)
            if custom_url:
                return Response({"short_url": custom_url.short_url})
        unique_id = get_unique_id()
        short_url = encode_base62(unique_id)
        request.data.update({"unique_id": unique_id, "short_url": short_url})
        print("Updated Data: ", request.data)
        serializer = CustomURLCreateSerializer(data=request.data)
        print("Serializer: ", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectURL(APIView):
    """
    get: get the long url snd redirect
    """
    def get(self, request,format=None, *args, **kwargs):
        short_url = self.kwargs.get("short_url")
        unique_id = decode_base62(short_url)
        print("Uniq: ", unique_id)
        long_url = CustomURL.get_long_url(unique_id)
        print(long_url)
        if long_url:
            return HttpResponseRedirect(redirect_to=long_url, status=status.HTTP_308_PERMANENT_REDIRECT)
        return Response({"message": "hello"})
