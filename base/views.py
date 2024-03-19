from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

ar=[{'name': "waga"}, {'name':'baga'}, {'name':'opir'}]


@api_view(['GET'])
def index(req):
    return Response({'msg':'hello'})


@api_view(['GET'])
def get_data(req):

    return Response(ar)