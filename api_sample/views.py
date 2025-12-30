from django.shortcuts import render,get_object_or_404

from api_sample.serializers import TodoSerializer

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import status

from api_sample.models import TodosampleModel

class TodoListCreate(APIView):

    def get(self,request):

        todo = TodosampleModel.objects.all()

        serializer = TodoSerializer(todo,many= True)

        return Response(serializer.data)
    
    def post(self,request):#body>>form-data>>

        serializer = TodoSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TodoUpdateRetrieveDeleteView(APIView):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        task =get_object_or_404(TodosampleModel,id=id)

        serializer = TodoSerializer(task,many = False)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):#get >> body >> raw >>instead of text >> json

        id = kwargs.get('pk')

        task = get_object_or_404(TodosampleModel,id=id)

        serializer = TodoSerializer(task,data=request.data)
    
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,**kwargs):

        id = kwargs.get('pk')

        task = get_object_or_404(TodosampleModel,id=id)

        task.delete()

        return Response({"message":"deleted successfully"},status=status.HTTP_200_OK)