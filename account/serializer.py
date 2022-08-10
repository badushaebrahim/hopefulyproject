from pyexpat import model
from rest_framework import serializers

from .models import CustomUser

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','username','email','password']
        # fields = '__all__'



class updateserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','password']