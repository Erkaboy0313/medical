from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response

# Create your views here.

class HomeView(viewsets.ViewSet):
    def list(self,request):
        return Response({'messgae':'hello'},status=status.HTTP_200_OK)
