from dataclasses import field
from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer




class CountrySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    # image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Country
        fields = ['id','name']
 
    def get__id(self, obj):
        return obj.id
 
    def get_name(self, obj):
        return obj.name 

    
class CustomerSerializer(serializers.ModelSerializer):
    FirstName = serializers.SerializerMethodField(read_only=True)
    LastName =   serializers.SerializerMethodField(read_only=True)
    Adress = serializers.SerializerMethodField(read_only=True)
    PhoneNumber = serializers.SerializerMethodField(read_only=True)
    Credit_Card_Number = serializers.SerializerMethodField(read_only=True)
    # User_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id','FirstName' ,'LastName' , 'Adress' , 'PhoneNumber' , 'Credit_Card_Number' , 'User_id' ]
    
    def get__id(self, obj):
        return obj.id

    def get_FirstName(self,obj):
        return obj.FirstName
    
    def get_LastName(self,obj):
        return obj.LastName
    
    def get_Adress(self,obj):
        return obj.Adress
    
    def get_PhoneNumber(self,obj):
        return obj.PhoneNumber
    
    def get_Credit_Card_Number(self,obj):
        return obj.Credit_Card_Number
    
    # def get_User_id(self,obj):
    #     return obj.User_id


class UserrSerializer(serializers.ModelSerializer):
    Username = serializers.SerializerMethodField(read_only=True)
    Password = serializers.SerializerMethodField(read_only=True)
    Email = serializers.EmailField(read_only=True)
    User_Role = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Userr
        fields = [  'Username' ,'Password' , 'Email' , 'User_Rolee' , '_id'  ]
    
    # def get__id(self, obj):
    #     return obj.id
    
    def get_Username(self,obj):
        return obj.Username
    
    def get_Password(self,obj):
        return obj.Password

    def get_Email(self,obj):
        return obj.Email

    def get_User_Role(self,obj):
        return obj.User_Role

    def get__id(self,obj):
        return obj._id
    

class UserRolesSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    Roles_Name = serializers.SerializerMethodField(read_only=True)
    # image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User_Roles
        fields = ['_id','Roles_Name']
 
    def get__id(self, obj):
        return obj.id
 
    def get_Roles_Name(self, obj):
        return obj.Roles_Name 
 

class Airline_companiesSerializer(serializers.ModelSerializer):
    Name = serializers.SerializerMethodField(read_only=True)
    Country_id = serializers.SerializerMethodField(read_only=True)
    User_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User_Roles
        fields = ['Name','Country_id' , 'User_id']
    
    def get_Name(self, obj):
        return obj.Name

    def get_User_id(self, obj):
        return obj.id
 
    def get_Country_id(self, obj):
        return obj.Country_id 




class FlightsSerializer(serializers.ModelSerializer):
    Airline_Company_Id = serializers.SerializerMethodField(read_only=True)
    Origin_Country_Id = serializers.SerializerMethodField(read_only=True)
    Destination_Country_Id = serializers.SerializerMethodField(read_only=True)
    Departure_Time = serializers.SerializerMethodField(read_only=True)
    Landing_Time = serializers.SerializerMethodField(read_only=True)
    Remaining_Tickets = serializers.SerializerMethodField(read_only=True)

    # def get_flights(self,obj):
    #     items = 



    class Meta:
        model = Userr
        fields = [  'Airline_Company_Id' ,'Origin_Country_Id' , 'Destination_Country_Id' , 'Departure_Time' , 'Landing_Time' , 'Remaining_Tickets'  ]
    
    # def get__id(self, obj):
    #     return obj.id
    
    def get_Origin_Country_Id(self,obj):
        return obj.Origin_Country_Id
    
    def get_Password(self,obj):
        return obj.Password

    def get_Destination_Country_Id(self,obj):
        return obj.Destination_Country_Id

    def get_Landing_Time(self,obj):
        return obj.Landing_Time

    def get_Remaining_Tickets(self,obj):
        return obj.Remaining_Tickets


class TicketSerializer(serializers.ModelSerializer):
    Flight_id = serializers.SerializerMethodField(read_only=True)
    Customer_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User_Roles
        fields = ['Flight_id','Customer_id']
 
    def get_Flight_id(self, obj):
        return obj.Flight_id
 
    def get_Customer_id(self, obj):
        return obj.Customer_id 

class AdministratorSerializer(serializers.ModelSerializer):
    FirstName = serializers.SerializerMethodField(read_only=True)
    LastName = serializers.SerializerMethodField(read_only=True)
    User_id = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User_Roles
        fields = ['FirstName','LastName' ,'User_id']
 
    def get_FirstName(self, obj):
        return obj.FirstName
 
    def get_LastName(self, obj):
        return obj.LastName 
   
    def get_User_id(self, obj):
        return obj.User_id 


