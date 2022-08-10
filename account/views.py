from pstats import Stats
from django.shortcuts import render
from account.serializer import loginserializer,updateserializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
        # print(request.data)
        try:
            userdatas= CustomUser.objects.get(username= request.data['username'],password = request.data['password'])
        except CustomUser.DoesNotExist:
            print("user not found")
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(type(userdatas))
        serializer = loginserializer(userdatas)
        # print(serializer.is_valid())
        # return Response(serializer.data)
        # print("new",serializer.data)
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


class user_Register(APIView):
    def post(self,request, *args, **kwargs):
        serial = loginserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class user_crud(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id,*args,**kwargs):
        print(request.user)
        error=False
        serial,error = get_userobj_byid_and_avalicheck(id,request)
        if error == True:
            return serial
        return Response(serial.data,status=status.HTTP_200_OK)
        
    

    def put(self,request,id,*args,**kwargs):
        userdatas= CustomUser.objects.get(pk=id)
        serial = loginserializer(userdatas,data=request.data)
        print(serial.is_valid())
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,*args,**kwargs):
        try:
            userdatas= CustomUser.objects.get(pk=id)
            serial = loginserializer(userdatas)
            # print(serial.data)
            print()
            if str(request.user) == str(serial.data["first_name"]):
                userdatas.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                print('else')
                return Response(status=status.HTTP_403_FORBIDDEN)
        except CustomUser.DoesNotExist:
            print("user not found")
            return Response(status=status.HTTP_404_NOT_FOUND)


    



# function to get object  by id and check if the user is the same my useing request.

def get_userobj_byid(id,request):
    try:
        userdatas= CustomUser.objects.get(pk=id)
        serial = loginserializer(userdatas)
        # print(serial.data)
        if str(request.user) == str(serial.data["first_name"]):
            return userdatas,False
        else:
            print('else')
            Response(status=status.HTTP_403_FORBIDDEN)
            return Response(status=status.HTTP_403_FORBIDDEN),True
    except CustomUser.DoesNotExist:
            print("user not found")
            return Response(status=status.HTTP_404_NOT_FOUND),True
    

def get_userobj_byid_and_avalicheck(id,request):

    try:
        userdatas= CustomUser.objects.get(pk=id)
        serial = loginserializer(userdatas)
        # print(serial.data)
        # print("req",request.user)
        # print("ser",serial.data["first_name"])
        if str(request.user) == str(serial.data["first_name"]):
            return serial,False
        else:
            print('else')
            return Response(status=status.HTTP_403_FORBIDDEN),True
        
    except CustomUser.DoesNotExist:
            print("user not found")
            return Response(status=status.HTTP_404_NOT_FOUND),True



@api_view(['GET','POST'])
def test_auth(request):
    if request.method == 'GET':
        return Response(request.data['user_id'])