from unicodedata import name
from ..serializers import   TicketSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Airline_companies ,  Ticket




@api_view(['GET','POST','PATCH','DELETE'])
def Tickets(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Ticket.objects.get(id = id)
                serializer_Tickets=TicketSerializer(productObj)
            except:
                return JsonResponse({"Ticket ID not found" : "Error"})
            return JsonResponse(serializer_Tickets.data , safe=False)
        else:
            if id==0:
                Tickets= Ticket.objects.all()
                serializer_Tickets=TicketSerializer(Tickets,many=True)
                return JsonResponse(serializer_Tickets.data , safe=False)
            return JsonResponse({"Ticket ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        # print(request.data)
        Flight_id =request.data['Flight_id'] 
        Customer_id = request.data['Customer_id']  
 

        Ticket.objects.create(Flight_id=request.data['Flight_id'] , Customer_id = request.data['Customer_id']  )
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Ticket.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Ticket.objects.get(id = id)
        temp.Flight_id  = request.data['Flight_id']
        temp.Customer_id = request.data['Customer_id'] 
   
        temp.save()
        return JsonResponse({'POST':"test"})