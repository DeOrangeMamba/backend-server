from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
 
    return Response(routes)
# from django.contrib.admin.views.decorators import staff_member_required staff_member_required
 
 

 
 
# # register
# def addUser(request):
#     User.objects.create_user(username='john2311',
#                                  email='jlen34non@beatl1es1.com',
#                                  password='gl44ass onion11')
#     return JsonResponse({"done":"tes"} )
 
 
 

 


 
 
 
 

 
 
 
