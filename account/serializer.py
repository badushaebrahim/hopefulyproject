from rest_framework import serializers

from .models import CustomUser

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','username','email','password','phone']
        # fields = '__all__'