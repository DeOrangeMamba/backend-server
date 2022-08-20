from unicodedata import name
from ..serializers import CountrySerializer , CustomerSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Country , Userr , Customer

@api_view(['GET','POST','PATCH','DELETE'])
def customer(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Customer.objects.get(id = id)
                serializer_customers=CustomerSerializer(productObj)
            except:
                return JsonResponse({"Customer ID not found" : "Error"})
            return JsonResponse(serializer_customers.data , safe=False)
        else:
            if id==0:
                customers=Customer.objects.all()
                serializer_customers=CustomerSerializer(customers,many=True)
                return JsonResponse(serializer_customers.data , safe=False)
            return JsonResponse({"Customer ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        # print(request.data)
        FirstName =request.data['FirstName'] 
        LastName = request.data['LastName'] 
        Adress = request.data['Adress'] 
        PhoneNumber = request.data['PhoneNumber']
        Credit_Card_Number = request.data['Credit_Card_Number'] 
        User_id= request.data['User_id']

        Customer.objects.create(FirstName=request.data['FirstName'] , LastName = request.data['LastName'] ,Adress = request.data['Adress'] , PhoneNumber = request.data['PhoneNumber'] , Credit_Card_Number = request.data['Credit_Card_Number'] , User_id= request.data['User_id'] )
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Customer.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Customer.objects.get(id = id)
        temp.FirstName =request.data['FirstName']
        temp.LastName = request.data['LastName']
        temp.Adress =request.data['Adress'] 
        temp.PhoneNumber = request.data['PhoneNumber']    
        temp.Credit_Card_Number = request.data['Credit_Card_Number'] 
        temp.User_id  = request.data['User_id']
        temp.save()
        return JsonResponse({'POST':"test"})