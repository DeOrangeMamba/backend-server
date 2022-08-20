from unicodedata import name
from ..serializers import CountrySerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Country , Userr

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({"test":"hello"})

def productSerialiaze(productObj):
    return {
                "Name":productObj.name,
                # "img":str( productObj.image), 
                }
                

# Create your views here.
@api_view(['GET','POST','PATCH','DELETE'])
def country(request,id=0):
    if request.method == 'GET': #method get all
        if int(id) > 0:
            try:
                productObj= Country.objects.get(id = id)
                serializer_countries=CountrySerializer(productObj)
            except:
                return JsonResponse({"country ID not found" : "Error"})
            return JsonResponse(serializer_countries.data , safe=False)
        else:
            if id==0:
                countries=Country.objects.all()
                serializer_countries=CountrySerializer(countries,many=True)
                return JsonResponse(serializer_countries.data , safe=False)
            return JsonResponse({"country ID not found" : "Error"})

    if request.method == 'POST': #method post add new row
        # try:
        print(request.data)
        
            # serializer=CountrySerializer(data=request.data)
        name =request.data['name']
    
        Country.objects.create(name=request.data['name']  )
        return JsonResponse({'POST':"test"})
        

    if request.method == 'DELETE': #method delete a row
        temp= Country.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PATCH': #method delete a row
        temp=Country.objects.get(id = id)
        temp.name =request.data['name']
        temp.save()
        return JsonResponse({'POST':"test"})


#     if serializer.is_valid():
        #         serializer.save()
        #         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        #     else:
        #         return Response(status=status.HTTP_400_BAD_REQUEST, data="Not Valid Data")
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data="Not Valid Data")