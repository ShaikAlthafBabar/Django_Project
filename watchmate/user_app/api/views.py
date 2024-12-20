from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 
from user_app.api.serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token
from user_app import models

@api_view(['POST'])
def logoutAV(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'],)
def registerAV(request):
    if(request.method=='POST'):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data={}
            data['response']='Registration Successfull'
            data['username']=account.username
            data['email']=account.email
            data['token'] = Token.objects.get(user=account).key
            return Response(data)
        else:
            raise ValidationError('{You have not provided correct data}')