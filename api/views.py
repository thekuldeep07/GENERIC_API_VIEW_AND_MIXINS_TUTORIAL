from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,


# Class for create and to fetch all list seperate as this not require PK

class CLStudentApi(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

#class for update , delete and retrieve as PK required

class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    


