from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
# Create your views here.

class ExpenseView(APIView):

    serializer_class = ExpenseSerializer

    def get(self,request,*args, **kwargs):

        query_set = Expense.objects.all()

        serializer = self.serializer_class(query_set,many=True) # SERIALIZATION: Converts Python queryset to Python native types (dict, list, etc.) which are then rendered into JSON.

        return Response(data=serializer.data)
    
    def post(self,request,*args, **kwargs):

        serializer = self.serializer_class(data=request.data) # DESERIALIZATION: Incoming JSON ➝ Python native types

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)