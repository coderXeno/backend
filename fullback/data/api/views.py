from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from data.models import Todoentriesmodel
from .serializers import TododataSerializer

class TodoAPI(APIView):
    @staticmethod
    def get(request,*args,**kwargs):
        entries = Todoentriesmodel.objects.all()
        serializer = TododataSerializer(entries, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    @staticmethod
    def post(request,*args,**kwargs):
        data = {
            'id': request.data.get('id'),
            'entry': request.data.get('entry')
        }

        serializer = TododataSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def snippet_detail(request, pk, format=None):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            snippet = Todoentriesmodel.objects.get(pk=pk)
        except Todoentriesmodel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TododataSerializer(snippet)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TododataSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

"""
@staticmethod
    def put(request, *args,**kwargs):
        data = {
            'id': request.data.get('id'),
            'entry': request.data.get('entry')
        }

        serializer = TododataSerializer(data=data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request,pk):
        try:
            entry = Todoentriesmodel.objects.get(pk=pk)
        except Todoentriesmodel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "DELETE":
            entry.delete()
            return Response("done",status=status.HTTP_202_ACCEPTED)
        return Response("failed",status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,format=None, *args,**kwargs):
        pk = self.kwargs.get('pk')
        todotask = Todoentriesmodel.objects.get(pk=pk)
        serializer = TododataSerializer(todotask, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""