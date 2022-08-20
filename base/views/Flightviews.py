from unicodedata import name
from ..serializers import CountrySerializer , FlightsSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Flights



@api_view(['GET','POST','PATCH','DELETE'])
def flight(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Flights.objects.get(id = id)
                serializer_Flightss=FlightsSerializer(productObj)
            except:
                return JsonResponse({"Flights ID not found" : "Error"})
            return JsonResponse(serializer_Flightss.data , safe=False)
        else:
            if id==0:
                Flightss=Flights.objects.all()
                serializer_Flightss=FlightsSerializer(Flightss,many=True)
                return JsonResponse(serializer_Flightss.data , safe=False)
            return JsonResponse({"Flights ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        # print(request.data)
        Airline_Company_Id =request.data['Airline_Company_Id'] 
        Origin_Country_Id = request.data['Origin_Country_Id']  
        Destination_Country_Id = request.data['Destination_Country_Id']  
        Departure_Time = request.data['Departure_Time']  
        Landing_Time = request.data['Landing_Time']  
        Remaining_Tickets = request.data['Remaining_Tickets']  



        Flights.objects.create(Airline_Company_Id=request.data['Airline_Company_Id'] , Origin_Country_Id = request.data['Origin_Country_Id']  ,
        Destination_Country_Id=request.data['Destination_Country_Id'] , Departure_Time=request.data['Departure_Time'] ,
        Landing_Time=request.data['Landing_Time'] ,Remaining_Tickets=request.data['Remaining_Tickets'] ,)
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Flights.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Flights.objects.get(id = id)
        temp.Airline_Company_Id  = request.data['Airline_Company_Id']
        temp.Origin_Country_Id = request.data['Origin_Country_Id'] 
        temp.Destination_Country_Id = request.data['Destination_Country_Id']    
        temp.Departure_Time = request.data['Departure_Time']    
        temp.Landing_Time = request.data['Landing_Time']    
        temp.Remaining_Tickets = request.data['Remaining_Tickets']   
        temp.save()
        return JsonResponse({'POST':"test"})