 
# , request
from rest_framework.decorators import api_view
# from django.contrib.auth. 
@api_view(['POST'])
def create (request):
    # user= User.objrcts.create_user(username=request.data["username"] ,password=request.data["password"] )

    return Response ({"reg":"test"})