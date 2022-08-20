"""myProjFly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


from . import views
# from .views import LoginView
# from .views import MyTokenObtainPairView

 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


# from myProjFly.base.models import Country


from .views import countryviews , customerviews , Userrviews , Ticketviews , Flightviews , LoginView, Administratorviews , AirlineCompaniesviews , UserRolesviews , CreateUserView

urlpatterns = [
    # path('ind', Userrviews.index),
    path('users', Userrviews.user),
    path('users/<id>', Userrviews.user),
    path('country/<str:id>',countryviews.country),
    path('country',countryviews.country),
    path('customer/<str:id>',customerviews.customer),
    path('customer',customerviews.customer),
    path('AirlineCompanies/<str:id>',AirlineCompaniesviews.Airlinecomps),
    path('AirlineCompanies',AirlineCompaniesviews.Airlinecomps),
    path('Administrator/<str:id>',Administratorviews.Admin),
    path('Administrator',Administratorviews.Admin),
    path('Flight/<str:id>',Flightviews.Flight),
    path('Flight',Flightviews.Flight),
    path('Ticket/<str:id>',Ticketviews.Tickets),
    path('Ticket',Ticketviews.Tickets),
    path('userrole/<str:id>',UserRolesviews.user_roles),
    path('userrole',UserRolesviews.user_roles),     
    # path('login/',LoginView.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login',TokenObtainPairView.as_view() ),


    # login
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]






