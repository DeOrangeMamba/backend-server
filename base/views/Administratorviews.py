from unicodedata import name
from ..serializers import   AdministratorSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Airline_companies , Administrator
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import permission_classes,api_view




@api_view(['GET','POST','PATCH','DELETE'])
def Admin(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Administrator.objects.get(id = id)
                serializer_Administrators=AdministratorSerializer(productObj)
            except:
                return JsonResponse({"Administrator ID not found" : "Error"})
            return JsonResponse(serializer_Administrators.data , safe=False)
        else:
            if id==0:
                Administrators=Administrator.objects.all()
                serializer_Administrators=AdministratorSerializer(Administrators,many=True)
                return JsonResponse(serializer_Administrators.data , safe=False)
            return JsonResponse({"Administrator ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        # print(request.data)
        FirstName =request.data['FirstName'] 
        LastName = request.data['LastName']  
        User_id = request.data['User_id']  

        Administrator.objects.create(FirstName=request.data['FirstName'] , LastName = request.data['LastName']  ,
        User_id=request.data['User_id'] )
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Administrator.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Administrator.objects.get(id = id)
        temp.FirstName  = request.data['FirstName']
        temp.LastName = request.data['LastName'] 
        temp.User_id = request.data['User_id']     
        temp.save()
        return JsonResponse({'POST':"test"})