from unicodedata import name
from ..serializers import CountrySerializer , Airline_companiesSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Airline_companies




@api_view(['GET','POST','PATCH','DELETE'])
def Airlinecomps(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Airline_companies.objects.get(id = id)
                serializer_Airline_companiess=Airline_companiesSerializer(productObj)
            except:
                return JsonResponse({"Airline_companies ID not found" : "Error"})
            return JsonResponse(serializer_Airline_companiess.data , safe=False)
        else:
            if id==0:
                Airline_companiess=Airline_companies.objects.all()
                serializer_Airline_companiess=Airline_companiesSerializer(Airline_companiess,many=True)
                return JsonResponse(serializer_Airline_companiess.data , safe=False)
            return JsonResponse({"Airline_companies ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        # print(request.data)
        Name =request.data['Name'] 
        Country_id = request.data['Country_id']  
        User_id = request.data['User_id']  

        Airline_companies.objects.create(Name=request.data['Name'] , Country_id = request.data['Country_id']  ,
        User_id=request.data['User_id'] )
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Airline_companies.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Airline_companies.objects.get(id = id)
        temp.Name  = request.data['Name']
        temp.Country_id = request.data['Country_id'] 
        temp.User_id = request.data['User_id']     
        temp.save()
        return JsonResponse({'POST':"test"})