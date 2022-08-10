from django.shortcuts import render
from account.serializer import loginserializer
from rest_framework import status

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
# from .serializer import loginserializer
class CustomAuthToken(ObtainAuthToken):

    # def post(self, request, *args, **kwargs):
    #     print(request.data["email"])
    #     #CustomUser.objects.get(email=request.data["email"],password=request.data["password"] )
    #     try:
    #         user = CustomUser.objects.get(email=request.data["email"],password=request.data["password"])
    #         # print("at mm",user.id)
    #         #return Response(user)
    #     except CustomUser.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serial = loginserializer(user)
    #     #serializer.is_valid(raise_exception=True)
    #     # if serial.is_valid(CustomUser,user):
    #     #     return Response(serial.data)
    #     # else:
    #     #     return  Response("error")
    #     # print(serial.is_valid(raise_exception=True))
    #     print(serial.data["username"])
    #     # serial.is_valid(raise_exception=True)
    #     # test =serial.validated_data['user']
    #     token, created = Token.objects.get_or_create(user=serial.data["username"])
    #     print(token)
    #     return Response(serial.data["username"])
    #     print(token)
    #     return Response({
    #         'token': token.key,
    #         'user_id': user.pk
    #     })
    def post(self, request, *args, **kwargs):
        # serializer = loginserializer(data=request.data)
        print(request.data)
        userdatas= CustomUser.objects.get(username= request.data['username'])
        print(type(userdatas))
        serializer = loginserializer(userdatas)

        # print(serializer.is_valid())
        # return Response(serializer.data)

        print("new",serializer.data)
        # print(serializer.is_valid())
        # user = serializer.validated_data['username']
        token, created = Token.objects.get_or_create(user=userdatas)
        print("-------------------------------------")
        # return Response({
        #     'token': token.key,
        #     'user_id': user.pk,
        #     'email': user.email
        # })
        data= {
            'token': token.key,
            'user_id':serializer.data["id"]
        }
        return Response(status=status.HTTP_200_OK,data=data)