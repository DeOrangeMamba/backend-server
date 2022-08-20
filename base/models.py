from pickle import TRUE
from random import choices
from django.db import models
from django.db import models
from django.contrib.auth.models import User
# from sqlalchemy import true
# from sqlalchemy import true
# from django.contrib.auth.models import User


class Country (models.Model):
    name=models.CharField(max_length=50,null=True,blank=True,unique=True)
    image = models.ImageField(upload_to='static',null=True,blank=True,default='/placeholder.png')


    
    def __str__(self):
        return self.name

class User_Roles(models.Model):
    id = models.IntegerField(primary_key=True)  # bigint, primary_key
    CUSTOMER='CR'
    AIRCOMP='AC'
    MANAGER='MR'
    CHOICES = [
        (CUSTOMER, 'Customer'),
        (AIRCOMP, 'Companies'),
        (MANAGER, 'Manager')
    ]
    role=models.CharField(max_length=2,choices=CHOICES,default=CUSTOMER)
    # Roles_Name = models.CharField(max_length=50, unique=True)  # text,unique
    
# class User_Role (models.Model):
#     CHOICES = ( 
#         ('Cus', 'Customer'),
#         ('AirComp', 'Companies'),
#         ('Man', 'Manager')
#     )
#     Role_Name=models.TextField(max_length=18,CHOICES=CHOICES)

    def __str__(self) :
        return self.role




class Userr(models.Model):
    Username=models.TextField(max_length=18,unique=True)
    Password=models.TextField(max_length=18)
    Email=models.TextField(max_length=50,unique=True)
    User_Rolee=models.ForeignKey(User_Roles,on_delete=models.CASCADE)
    # IMG = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    # image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self) :
        return '{} {}'.format(self.Username,self.User_Rolee)


class Airline_companies (models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Country_id= models.ForeignKey(Country,on_delete=models.CASCADE)
    User_id=models.OneToOneField(Userr,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Name

class Flights (models.Model):
    Airline_Company_Id=models.ForeignKey(Airline_companies,on_delete=models.CASCADE)
    Origin_Country_Id=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='Origin')
    Destination_Country_Id=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='Destination')
    Departure_Time=models.DateTimeField()
    Landing_Time=models.DateTimeField()
    Remaining_Tickets=models.IntegerField()

    def __str__ (self):
        return str(self.id)

class Customer (models.Model):
    FirstName=models.TextField(max_length=13)
    LastName=models.TextField(max_length=18)
    Adress=models.TextField(max_length=18)
    PhoneNumber=models.TextField(max_length=14)
    Credit_Card_Number=models.TextField(max_length=30 ,unique=True)
    User_id=models.OneToOneField(Userr,on_delete=models.CASCADE,unique=True)

    def __str__(self):
        return '{} {}'.format(self.FirstName,self.LastName)

class Ticket (models.Model):
    Flight_id=models.OneToOneField(Flights,on_delete=models.CASCADE,unique=True)
    Customer_id=models.OneToOneField(Userr,on_delete=models.CASCADE,unique=True)

    def __str__(self):
        return f'Flight ID is {str(self.Flight_id)} , Customer ID :{str(self.Customer_id)} '

class Administrator (models.Model):
        FirstName=models.TextField(max_length=13)
        LastName=models.TextField(max_length=18)
        User_id=models.OneToOneField(Userr,on_delete=models.CASCADE,unique=True)
        
        def __str__(self):
            return self.FirstName


# class Profile(models.model):
#     avatar = 
#     adress = 







