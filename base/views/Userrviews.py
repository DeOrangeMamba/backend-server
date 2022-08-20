from unicodedata import name
from ..serializers import CountrySerializer , UserrSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Country , Userr , Customer, User_Roles


@api_view(['GET','POST','PATCH','DELETE'])
def user(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Userr.objects.get(id = id)
                serializer_Userrs=UserrSerializer(productObj)
            except:
                return JsonResponse({"Userr ID not found" : "Error"})
            return JsonResponse(serializer_Userrs.data , safe=False)
        else:
            if id==0:
                Userrs=Userr.objects.all()
                serializer_Userrs=UserrSerializer(Userrs,many=True)
                return JsonResponse(serializer_Userrs.data , safe=False)
            return JsonResponse({"Userr ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        print(request.data)
        Username =request.data['Username'] 
        Password = request.data['Password'] 
        Email = request.data['Email'] 
        User_Role = request.data['User_Role']
        # _id = request.data['_id'] 


        role_id = 0
        print(request.data)

        if request.data['User_Role'] == 'Customer':
            role_id = 1
        elif request.data['User_Role'] == 'Company':
            role_id = 2
        elif request.data['User_Role'] == 'Manager':
            role_id = 3
        print('line 47')
        print('\n\n\nthe role id is:', role_id, '\n\n\n')
        print('line 49')


        User_Role = User_Roles.objects.get(id=role_id)
        print(User_Role)
        newuser=Userr.objects.create(Username=request.data['Username'] , Password = request.data['Password'] ,Email = request.data['Email'],User_Rolee=User_Role  )
        # newuser.User_Rolee=User_Role
        return JsonResponse({'status':201})
        

    if request.method == 'DELETE': #method delete a row
        temp= Userr.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Userr.objects.get(id = id)
        temp.Username =request.data['Username']
        temp.Password = request.data['Password']
        temp.Email =request.data['Email'] 
        temp.User_Role = request.data['User_Role']    
        temp._id  = request.data['_id']
        temp.save()
        return JsonResponse({'POST':"test"})