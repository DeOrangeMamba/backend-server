from unicodedata import name
from ..serializers import CountrySerializer , UserRolesSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Country , User_Roles , Customer , User_Roles



@api_view(['GET','POST','PATCH','DELETE'])
def user_roles(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= User_Roles.objects.get(id = id)
                serializer_User_Roless=UserRolesSerializer(productObj)
            except:
                return JsonResponse({"User_Roles ID not found" : "Error"})
            return JsonResponse(serializer_User_Roless.data , safe=False)
        else:
            if id==0:
                User_Roless=User_Roles.objects.all()
                serializer_User_Roless=UserRolesSerializer(User_Roless,many=True)
                return JsonResponse(serializer_User_Roless.data , safe=False)
            return JsonResponse({"User_Roles ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        # print(request.data)
        id =request.data['id'] 
        Roles_Name = request.data['Roles_Name']  


        User_Roles.objects.create(id=request.data['id'] , Roles_Name = request.data['Roles_Name']  )
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= User_Roles.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=User_Roles.objects.get(id = id)
        temp.id  = request.data['id']
        temp.Roles_Name = request.data['Roles_Name']    
        temp.save()
        return JsonResponse({'POST':"test"})