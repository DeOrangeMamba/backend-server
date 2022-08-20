from django.contrib import admin
from .models import Airline_companies,Flights,Country,Customer,Ticket,Administrator, User_Roles, Userr
# Register your models here.
admin.site.register(Airline_companies)
admin.site.register(Customer)
admin.site.register(Flights)
admin.site.register(Ticket)
admin.site.register(Administrator)
admin.site.register(User_Roles)
admin.site.register(Country)
admin.site.register(Userr)