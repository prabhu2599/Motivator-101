from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .models import AstroModel
from .serializer import AstroSerializer
from rest_framework.views import APIView
from random import randint
# Create your views here.


class AstroView(APIView):

    def get(self,request):
        astro = AstroModel.objects.get(id=randint(1, 10))
        serializer = AstroSerializer(astro)
        return Response(serializer.data)

    def post(self,request):
        serializer = AstroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AstroAll(APIView):

    def get(self,request):
        astro = AstroModel.objects.all()
        serializer = AstroSerializer(astro, many=True)
        return Response(serializer.data)